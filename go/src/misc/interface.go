package main

import (
    "fmt"
)
type Interface interface{
    testFunc()
}
type S struct{
    name string
    id int
}
func (s *S) testFunc(){
    fmt.Print(s)
}

func showit(inte Interface){
    if s1, ok := inte.(*S);ok{
        s1.testFunc()
    }
}

func main(){
    s := S{name:"testname", id:12}
    var i Interface
    i = &s
    i.testFunc()
}
/*
package main

type Shower interface {
    Show()
}

type S1 struct {
}

func (this *S1) Show() {
    println("Show from S1")
}

func InvokeShow(s Shower) {
    if s1, ok := s.(*S1); ok {
        s1.Show()
    }
}

func main() {
    var s1 S1
    InvokeShow(&s1)
}
*/
