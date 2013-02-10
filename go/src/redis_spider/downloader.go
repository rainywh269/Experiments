package main

import(
    dwler "downloader"
)

type Parser interface {
    Start() chan string
    AfterFinished(url string)
}

type Downloader interface{
    Download(url string) []byte
}

type ImgResource interface{
    GetUrl() string
}

type Content struct{
    Content []byte
    Resource ImgResource
}

func MakeDownloaderWorkers(worker_factory func() Downloader) chan *Downloader{
    worker_pool := make(chan *Downloader, CONCURENT_DOWNLOADS)
    for i:=0;i<CONCURENT_DOWNLOADS;i++{
        downloader := worker_factory()
        worker_pool <- &downloader
    }
    return worker_pool
}

func ProxyDownloaderFactory() Downloader{
    downloader := dwler.MakePDownloader(HTTP_PROXY)
    return downloader
}

func DirectDownloaderFactory() Downloader{
    downloader := dwler.DDownloader{}
    return downloader
}

func Download_raw(img_resource ImgResource, td TumblrDownloader){
    worker := *(<- worker_pool)
    defer func(){
        worker_pool <- &worker
    }()
    content := worker.Download(img_resource.GetUrl())
    if len(content) > 0{
        result := Content{
            Content:content,
            Resource:img_resource,
        }
        td.ContenChan <- result
    }else{
        td.UrlChan <- img_resource
    }
}
