package main

import "fmt"

type Vertex struct {
    Lat, Long float64
}

//var m map[string]Vertex

func main() {
    m := map[string]Vertex{}
    m["Bell Labs"] = Vertex{
        40.68433, 74.39967,
    }
    fmt.Println(m["Bell Labs"])
    test, ok := m["test"]
    fmt.Println(test)
    fmt.Println(ok)
}
