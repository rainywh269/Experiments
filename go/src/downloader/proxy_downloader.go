package downloader

import(
    "log"
    "net/http"
    "net/url"
    "io/ioutil"
)

type PDownloader struct{
    client *http.Client
}

func MakePDownloader(proxy_url string) PDownloader{
    client := GetDoubanProxyClient(proxy_url)
    return PDownloader{&client}
}

func GetDoubanProxyClient(url string) http.Client{
    return ProxyDownloader(url)
}

func ProxyDownloader(proxyUrl string) http.Client{
    url, _ := url.Parse(proxyUrl)
    proxy := http.ProxyURL(url)
    tr := http.Transport{Proxy:proxy}
    client := http.Client{Transport:&tr}
    return client
}

func (self PDownloader) Download(url string)([]byte){
    log.Printf("Downloading with proxy : %s", url)
    rst, err := self.client.Get(url)
    if err != nil{
        log.Println(err)
        return []byte{}
    }
    data, err := ioutil.ReadAll(rst.Body)
    if err != nil{
        log.Println(err)
        return []byte{}
    }
    log.Printf("Downloading with proxy Completed : %s", url)
    return data
}
