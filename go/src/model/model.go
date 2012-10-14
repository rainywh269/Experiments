package model

import(
    "fmt"
)

type Author struct{
    Id int
    Name string
}
type Post struct{
    Id int
    Author Author
    Title, Body string
}
type Note struct{
    Post
    Img string
}

func Test(in int){
    print(in)
}

func (p Author) Author(){
    fmt.Println("author:" + p.Name)
}
