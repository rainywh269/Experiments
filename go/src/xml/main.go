package main

import (
    "io/ioutil"
    "fmt"
    "regexp"
    "strings"
)

func main(){
    //atom, _ := os.Open("atom")
    //defer atom.Close()
    atom, _ := ioutil.ReadFile("atom")
    data := string(atom)

    finder, _ := regexp.Compile(`src="(.*?)"`)
    
    rslts := finder.FindAllStringSubmatch(data, -1)
    for _, v := range rslts{
        url := v[1]
        url = strings.Replace(url, "_500", "_1280", -1)
        fmt.Println(url)
    } 
}

