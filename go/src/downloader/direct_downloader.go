package downloader

import(
    "net/http"
    "io/ioutil"
)

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
