package downloader

import(
    "fmt"
    "testing"
)

func TestDownloadWithProxy(t *testing.T){
    fmt.Println("hello")
    data := DownloadWithProxy("http://4chan.org")
    fmt.Println(string(data))
}

