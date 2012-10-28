package downloader

import(
    "fmt"
    "net/http"
    "net/url"
    "io/ioutil"
)

var Downloader *http.Client = nil

func ProxyDownloader(proxyUrl string) *http.Client{
    url, _ := url.Parse(proxyUrl)
    proxy := http.ProxyURL(url)
    tr := http.Transport{Proxy:proxy}
    client := &http.Client{Transport:&tr}
    return client
}

func GetDoubanProxyClient() http.Client{
    if Downloader == nil{
        //Downloader = ProxyDownloader("http://10.8.0.1:8118/")
        Downloader = ProxyDownloader("http://vpn2:8118/")
    }
    return *Downloader
}

func DownloadWithProxy(url string) []byte{
    client := GetDoubanProxyClient()
    rst, err := client.Get(url)
    if err != nil{
        fmt.Println(err)
        return []byte{}
    }
    data, err := ioutil.ReadAll(rst.Body)
    if err != nil{
        fmt.Println(err)
        return []byte{}
    }
    return data
}

func Download(url string) []byte{
    rst,_ :=  http.Get(url)
    data,_ := ioutil.ReadAll(rst.Body)
    return data
}
