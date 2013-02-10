package main

import(
)

var worker_pool chan *Downloader
var exit_signal chan int

func main(){
    recorder := CreateSqliteRecorder(SQLITE_FILE)
    //recorder := CreateRedisRecord(REDIS_NETWORK, REDIS_LOCATION)
    tumblr_sources := parse_tumblr_sources()
    worker_pool = MakeDownloaderWorkers(DirectDownloaderFactory)
    for _, tumblr_source := range tumblr_sources{
        td := MakeTumblrDownloader(tumblr_source.Name, tumblr_source.Suffix, tumblr_source.Url, &recorder)
        go td.Start()
    }
    a:=make(chan int)
    <-a
}

