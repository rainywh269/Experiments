package main

import (
    "model"
    "fmt"
)

func main(){
    var author=model.Author{Id:1,Name:"wooparadog"}
    var d = model.Note{
        Post:model.Post{
            Id:1,
            Author:author,
            Title:"titlepa",
            Body:"body",
        },
        Img:"img" }

    d.Author.Name = "testAuthor"
    d.Author.Author()

    fmt.Println(d.Title)
}
