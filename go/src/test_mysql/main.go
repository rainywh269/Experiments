package main

import (
    "fmt"
    "database/sql"
    /*_ "code.google.com/p/go-mysql-driver/mysql"*/
    _ "github.com/mattn/go-sqlite3"
)

type Subject struct{
    Id int
    Name string
}

func main(){
    //#fmt.Println("hello world")
    //db, _ := sql.Open("mysql", "root:localhost@tcp(127.0.0.1:3306)/test_wooparadog9010?charset=utf8") 
    db, _ := sql.Open("sqlite3", "data.sqlite3")
    defer db.Close()

    /*r, _ := db.Exec("select * from subject")*/
    r, err := db.Query("select id, uid from subject")

    if err != nil{
        fmt.Println(err)
        _, err := db.Exec("create table subject( id int(2), uid text)")
        fmt.Println(err)
    }

    results := make([]Subject, 0)
    for r.Next(){
        var subject Subject
        r.Scan(&subject.Id, &subject.Name)
        results = append(results, subject)
    }

    fmt.Println(len(results))
    for _,v := range results{
        fmt.Println(v.Id, v.Name)
    }

    transaction, _ := db.Begin()
    st, err := transaction.Prepare("insert into subject (id, uid) values (21,'the2')")
    if err!=nil{
        fmt.Println(err)
        return
    }
    transaction.Stmt(st).Exec()
    transaction.Commit()
}

