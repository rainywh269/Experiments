package main

import(
    "fmt"
    //"downloader"
)

func main(){
    //data := downloader.DownloadWithProxy("http://4chan.org")
    a := make([]int, 0)
    b := []int{1,2,3,4,5}

    c := append(append(a, 999), b...)
    
    fmt.Println(c)
}
