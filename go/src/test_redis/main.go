package main

import(
    redis "github.com/garyburd/redigo/redis"
    "fmt"
)

func main(){
    connction, _ := redis.Dial("unix", "/tmp/redis.sock") 
    defer connction.Close()

    //connction.Do("set", "tests", "1")
    d,err :=  connction.Do("get", "tests")
    fmt.Println(d,err)

}
