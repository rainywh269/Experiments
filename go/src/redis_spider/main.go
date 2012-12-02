package main

import(
    "fmt"
)

var worker_pool chan *Downloader

func main(){
    td := MakeTumblrDownloader("melc", "_500", "http://melc.tumblr.com/rss")
    url_chan, content_chan := td.GetTargetUrlChannel()
    worker_pool = MakeDownloaderWorkers(ProxyDownloaderFactory)
    for {
        url, err := <-url_chan
        if !err {
            break
        }
        go download(url, content_chan)
    }
}

func download(url string, content_chan chan Content){
    fmt.Println( url, "downloading")
    worker := *(<- worker_pool)
    defer func(){
        worker_pool <- &worker
    }()
    content := worker.Download(url)
    if len(content) > 0{
        result := Content{
            Content:content,
            Url:url,
        }
        content_chan <- result 
    }
}
