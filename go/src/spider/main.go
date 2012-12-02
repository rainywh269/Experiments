package main

import(
    "path"
    "os"
    "downloader"
    "container/list"
    "fmt"
    "regexp"
    "strings"
    "io/ioutil"
)
type worker func(n list.Element)
var ch chan list.Element
var melc_worker chan worker

func main(){
    download_melc()
}

func getWorkers(){
    for i:=0;i<3;i++{
        melc_worker <- melc_channel_worker
    }
}
func download_urls(urls *list.List){
    for e := urls.Front(); e != nil; e = e.Next(){
        p_worker := <- melc_worker
        go p_worker(*e)
    }
}

func download_melc(){
    ch = make(chan list.Element) 
    melc_worker = make(chan worker)
    url := "http://melc.tumblr.com/rss"
    body := string(downloader.DownloadWithProxy(url))
    urls := parse_melc(body)
    go getWorkers()
    go download_urls(urls)
    for {
        req := <- ch
        urls.Remove(&req)
        if urls.Len()==0{
            break
        }
    }
}

func melc_channel_worker(n list.Element){
    url := n.Value.(string)

    dir, _ := os.Getwd()
    dir = path.Join(dir, "melc")
    _, err := os.Stat(dir)
    _, ok := err.(*os.PathError)
    if ok{
        fmt.Println("make dir", dir)
        os.MkdirAll(dir, 0775) 
    }

    filename := path.Base(url)
    filename = path.Join(dir, filename)

    fmt.Println("downloading", n.Value.(string), filename)

    _, err = os.Stat(filename)
    _, ok = err.(*os.PathError)
    if ok{
        data, err := downloader.Download(url)
        if err{
            ioutil.WriteFile(filename, data, 0600)
        }
    }else{
        fmt.Println("Already downloaded")
    }
    ch <- n
    melc_worker <- melc_channel_worker
}

func parse_melc(body string) *list.List{
    results := list.New()
    finder, _ := regexp.Compile(`src="(.*?)"`)

    rslts := finder.FindAllStringSubmatch(body, -1)
    for _, v := range rslts{
        url := v[1]
        url = strings.Replace(url, "_500", "_1280", -1)
        results.PushBack(url)
    }
    return results
} 
