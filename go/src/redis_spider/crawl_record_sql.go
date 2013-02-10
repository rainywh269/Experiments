package main

import(
    "log"
    "sync"
    "database/sql"
    _ "github.com/mattn/go-sqlite3"
)

type SqliteRecorder struct{
    conn *sql.DB
    mutex sync.Mutex
}

func CreateSqliteRecorder(network, location string) SqliteRecorder{
    conn, err := sql.Open("sqlite3", SQLITE_FILE)
    if err != nil {
        log.Fatal("Sqlite connection fail!\nFile: ", SQLITE_FILE)
    }
    _, err = conn.Exec("create table download_record if not exists(url varchar(512) primary key) ")
    if err != nil{
        log.Fatal("Sqlite Recorder Table download_record does not exists and cannot be created")
    }
    log.Println("Sqlite Recorder Connected")
    return SqliteRecorder{conn: conn}
}


func (self *SqliteRecorder) MarkAsFinished(url string){
    self.mutex.Lock()
    self.mutex.Unlock()
}

func (self *SqliteRecorder) HasFinished(url string) bool{
    self.mutex.Lock()
    row := self.conn.QueryRow("select url from download_record where url =%s", url)
    self.mutex.Unlock()
    log.Fatal(">>>>>", row)
    return true
}
