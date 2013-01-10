package main

import(
    "os"
    "io/ioutil"
    "fmt"
    "path"
    "strings"
    "regexp"
    "time"
)


type TumblrDownloader struct{
    recorder *RedisRecorder
    name string
    rss_img_size string
    rss_addr string
}

func MakeTumblrDownloader(name, rss_img_size, rss_addr string) TumblrDownloader{
    recorder := CreateRedisRecord(REDIS_NETWORK, REDIS_LOCATION)
    downloader := TumblrDownloader{
        recorder:&recorder,
        name:name,
        rss_img_size:rss_img_size,
        rss_addr:rss_addr,
    }
    return downloader
}

func (self *TumblrDownloader) AfterFinished(content_chan chan Content){
    dir, _ := os.Getwd()
    dir = path.Join(dir, self.name)
    _, err := os.Stat(dir)
    _, ok := err.(*os.PathError)
    if ok{
        fmt.Println("make dir", dir)
        os.MkdirAll(dir, 0775) 
    }
    for {
        content := <- content_chan
        filename := path.Base(content.Url)
        filename = path.Join(dir, filename)
        ioutil.WriteFile(filename, content.Content, 0600)
        self.recorder.MarkAsFinished(content.Url)
        fmt.Println("[LOG] New Download Finished", content.Url)
    }
}

func (self *TumblrDownloader) process_url(url string, url_chan chan string){
    url = strings.Replace(url, "_500", "_1280", -1)
    if !self.recorder.HasFinished(url){
        url_chan <- url
    }else{
        fmt.Println("[LOG] Already Downloaded", url)
    }
}

func (self *TumblrDownloader) check_rss(url_chan chan string){
    p_downloader := ProxyDownloaderFactory()
    for {
        finder, _ := regexp.Compile(`src="(.*?)"`)
        body := string(p_downloader.Download(self.rss_addr))
        rslts := finder.FindAllStringSubmatch(body, -1)
        for _, v := range rslts{
            url := v[1]
            go self.process_url(url, url_chan)
        }
        time.Sleep(CHECK_INTERVAL)
    }
}

func (self *TumblrDownloader) GetTargetUrlChannel() (chan string, chan Content){
    url_chan := make(chan string) 
    content_chan := make(chan Content) 
    go self.check_rss(url_chan)
    go self.AfterFinished(content_chan)
    return url_chan, content_chan
}
