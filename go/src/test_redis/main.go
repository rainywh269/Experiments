package main

import(
    redis "github.com/garyburd/redigo/redis"
    "fmt"
)

func main(){
    connction, err := redis.Dial("unix", "/tmp/redis.sock") 
    defer connction.Close()

    connction.Do("set", "test", 5)
    connction.Receive()
    
    fmt.Println(err)

}
