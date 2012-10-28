package main

import(
    "fmt"
    "downloader"
)

func main(){
    data := downloader.DownloadWithProxy("http://4chan.org")
    fmt.Println(string(data))
}
