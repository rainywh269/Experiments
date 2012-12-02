package main

import(
    "os"
    "io/ioutil"
    "fmt"
    "path"
    "strings"
    "regexp"
    RawDownloader "downloader"
)

type RedisRecorder struct{
    Network string
    Location string
}

type TumblrDownloader struct{
    recorder *RedisRecorder
    name string
    rss_img_size string
    rss_addr string
}

func MakeTumblrDownloader(name, rss_img_size, rss_addr string) TumblrDownloader{
    recorder := RedisRecorder{
        Network:REDIS_NETWORK,
        Location:REDIS_LOCATION,
    }
    downloader := TumblrDownloader{
        recorder:&recorder,
        name:name,
        rss_img_size:rss_img_size,
        rss_addr:rss_addr,
    }
    return downloader
}

func (self TumblrDownloader) AfterFinished(content_chan chan Content){
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
        fmt.Println("finished", content.Url)

        filename := path.Base(content.Url)
        filename = path.Join(dir, filename)
        fmt.Println("saving", content.Url, filename)
        ioutil.WriteFile(filename, content.Content, 0600)

    }
}

func (self TumblrDownloader) check_rss(url_chan chan string){
    finder, _ := regexp.Compile(`src="(.*?)"`)

    body := string(RawDownloader.DownloadWithProxy(self.rss_addr))
    rslts := finder.FindAllStringSubmatch(body, -1)
    for _, v := range rslts{
        url := v[1]
        url = strings.Replace(url, "_500", "_1280", -1)
        fmt.Println(url)
        url_chan <- url
    }
}

func (self TumblrDownloader) GetTargetUrlChannel() (chan string, chan Content){
    url_chan := make(chan string) 
    content_chan := make(chan Content) 
    go self.check_rss(url_chan)
    go self.AfterFinished(content_chan)
    return url_chan, content_chan
}
