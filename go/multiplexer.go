package main

import (
    "fmt"
)

type request struct {
    a, b int
    replyc chan int
}

func (r *request) String() string {
    return fmt.Sprintf("%d+%d=%d",
    r.a, r.b, <-r.replyc)
}

type binOp func(a, b int) int

func run(op binOp, req *request) {
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
    req.replyc <- op(req.a,req.b)
}
func server(op binOp, service <-chan *request) {
    for {
        req := <-service // requests arrive here
        go run(op, req) // don't wait for op
    }
}
func startServer(op binOp) chan<- *request {
    service := make(chan *request)
    go server(op, service)
    return service
}
func main(){
    adderChan := startServer( func(a, b int) int { return a + b }) 
    req1 := &request{7, 8, make(chan int)}
    req2 := &request{17, 18, make(chan int)}
    adderChan <- req1
    adderChan <- req2
    fmt.Print(req1,req2)
}


