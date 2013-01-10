package main

import(
)

var worker_pool chan *Downloader

func main(){
    td := MakeTumblrDownloader("fantastic", "_500", "http://pornisfantastic.tumblr.com/rss")
    url_chan, content_chan := td.GetTargetUrlChannel()
    worker_pool = MakeDownloaderWorkers(DirectDownloaderFactory)
    for {
        url, err := <-url_chan
        if !err {
            break
        }
        go download(url, content_chan, url_chan)
    }
}

func download(url string, content_chan chan Content, url_chan chan string){
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
    }else{
        url_chan <- url
    }
}
