package redis

import (
    redis "github.com/garyburd/redigo/redis"
    "fmt"
)

type Redis struct{
    Network string
    Location string
    conn *redis.Conn
}

func (self *Redis) Connect() bool{
    fmt.Println(self.Network, self.Location)
    for i:=0;i<3;i++{
        conn, err  := redis.Dial(self.Network, self.Location)
        if err == nil {
            self.conn = &conn
            return true
        }else{
            fmt.Println(err)
        }
    }
    return false
}

func prepareCommand(name string, args []interface{}) []interface{}{
    new_para := make([]interface{}, 0)
    new_para = append(append(new_para, name), args...)
    return new_para
}

func (self *Redis) Sadd(name string, args ...interface{}){
    args = prepareCommand(name, args)
    _, err := (*self.conn).Do("sadd", args...)
    if err != nil{
        fmt.Println("[ERROR] Sadd Failed, msg:", err, "key:", name, "args:", args)
    }
}

func (self *Redis) Sismember(name string, arg ...interface{}) bool{
    arg = prepareCommand(name, arg)
    result, err := (*self.conn).Do("sismember", arg...)

    if err != nil{
        fmt.Println("[ERROR] Sismember Failed, msg:", err, "key:", name, "arg:", arg)
        return false
    }

    if result.(int64) == 1{
        return true
    }

    return false
}


func (self Redis) Close(){
    (*self.conn).Close()
}
