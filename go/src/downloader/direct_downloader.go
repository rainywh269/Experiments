package downloader

import(
    "net/http"
    "io/ioutil"
)


func Download(url string) ([]byte, int){
    rst,err :=  http.Get(url)
    data  := []byte{}
    end_err := 1
    if err != nil{
        raw_data,err_io := ioutil.ReadAll(rst.Body)
        if err_io != nil{
            data = raw_data
            end_err = 0
        }
    }
    return data, end_err
}
