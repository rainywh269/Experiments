package main

import (
    "fmt"
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
    d.author.author()

    fmt.Println(d.title)
}
func (p Author) author(){
    fmt.Println("author:" + p.name)
}
