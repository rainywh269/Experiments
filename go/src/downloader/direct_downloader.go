package downloader

import(
    "net/http"
    "io/ioutil"
    "log"
)

type DirectDownloader struct{
    client *http.Client
}

type DDownloader struct{}

func (self DDownloader) Download(url string)([]byte){
    rst,err :=  http.Get(url)
    data  := []byte{}
    if err == nil {
        raw_data, err_io := ioutil.ReadAll(rst.Body)
        if err_io == nil{
            data = raw_data
        }
    }
    return data
}

func MakeDirectDownloader(timeout int64) DirectDownloader{
    client := http.Client{
        Transport: &http.Transport{
            Dial: timeoutDialler(timeout),
        },
    }
    return DirectDownloader{&client}
}

func (self DirectDownloader) Download(url string)([]byte){
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


//func main() {
//    c := http.Client{
//        Transport: &http.Transport{
//            Dial: timeoutDialler(1e9),
//        },
//    }
//    r, err := c.Get("http://google.com/")
//    if err != nil {
//        log.Fatal("get: ", err)
//    }
//    io.Copy(os.Stdout, r.Body)
//}
