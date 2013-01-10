package main

import(
    dwler "downloader"
)

type Parser interface {
    GetTargetUrlChannel() chan string
    AfterFinished(url string)
}

type Downloader interface{
    Download(url string) []byte
}

type Content struct{
    Content []byte
    Url string
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
