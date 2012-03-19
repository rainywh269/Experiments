package main

import (
    "fmt"
    "blackfriday"
)
type Author struct{
    id int
    name string
}
type Post struct{
    id int
    author Author
    title, body string
}
type Note struct{
    Post
    img string
}

type A struct {
    ax, ay int
}
type B struct {
    A
    bx, by float64
}
type C interface{
    author()
}

func main(){
    var author=Author{id:1,name:"wooparadog"}

    var d = Note{
        Post:Post{
            id:1,
            author:author,
            title:"titlepa",
            body:"body",
        }, 
        img:"img" }

    d.author.name = "testAuthor"

    fmt.Println(d.title)
    var ai C
    ai = d.author
}
func (p Author) author(){
    fmt.Print("author:" + p.name)
}
