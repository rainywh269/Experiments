package main

import(
    "fmt"
    "time"
    "container/list"
)

var ch chan list.Element

func channel_worker(n list.Element){
    time.Sleep(time.Duration(n.Value.(int))*time.Second)
    fmt.Println("out", n)
    ch <- n
}

func main(){
    ch = make(chan list.Element) 
    a := list.New()
    a.PushBack(5)
    a.PushBack(4)
    a.PushBack(3)
    a.PushBack(2)
    a.PushBack(1)
    for e := a.Front(); e != nil; e = e.Next(){
        fmt.Println("in", e)
        go channel_worker(*e)
    }
    fmt.Println(a)
    for {
        req := <- ch
        a.Remove(&req)
        if a.Len()==0{
            break
        }
    } 
}

