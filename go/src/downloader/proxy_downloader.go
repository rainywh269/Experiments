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

func MakePDownloader(proxy_url string, timeout int64) PDownloader{
    client := ProxyDownloader(proxy_url, timeout)
    return PDownloader{&client}
}


func ProxyDownloader(proxyUrl string, timeout int64) http.Client{
    url, _ := url.Parse(proxyUrl)
    proxy := http.ProxyURL(url)
    tr := http.Transport{
        Proxy:proxy,
        Dial: timeoutDialler(timeout),
    }
    client := http.Client{Transport:&tr}
    return client
}

func (self PDownloader) Download(url string)([]byte){
    rst, err := self.client.Get(url)
    if err != nil{
        log.Println("Connect Error: ", err)
        return []byte{}
    }
    data, err := ioutil.ReadAll(rst.Body)
    if err != nil{
        log.Println("Response Error: ", err)
        return []byte{}
    }
    return data
}
