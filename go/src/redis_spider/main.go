package main

import(
)

var worker_pool chan *Downloader


func main(){
    tumblr_sources := parse_tumblr_sources()
    worker_pool = MakeDownloaderWorkers(DirectDownloaderFactory)
    for _, tumblr_source := range tumblr_sources{
        td := MakeTumblrDownloader(tumblr_source.Name, tumblr_source.Suffix, tumblr_source.Url)
        url_chan, content_chan := td.GetTargetUrlChannel()
        for {
            url, err := <-url_chan
            if !err {
                break
            }
            go download(url, content_chan, url_chan)
        }
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
