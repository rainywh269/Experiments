package main

import (
    "time"
    "os"
    "log"
    "path"
    "io"
    "fmt"
    "encoding/json"
)
const CONCURENT_DOWNLOADS = 4

const REDIS_NETWORK = "unix"
const REDIS_LOCATION = "/tmp/redis.sock"

const SQLITE_FILE = "data.sqlite3"

const HTTP_PROXY = "http://10.8.0.1:8118"
const CHECK_INTERVAL = time.Minute * 1
const SET_NAME = "url_set"

type TumblrSource struct{
    Name string
    Suffix string
    Url string
}

func parse_tumblr_sources() []TumblrSource{
    sources := make([]TumblrSource, 0)
    dir, _ := os.Getwd()
    config_file := path.Join(dir, "config.json")
    config, _ := os.Open(config_file)
    config_decoder := json.NewDecoder(config)
    fmt.Println("Parsing tumblr sources...")
    for {
        var m TumblrSource
        if err := config_decoder.Decode(&m); err == io.EOF {
            break
        } else if err != nil {
            log.Fatal(err)
        }
        sources = append(sources, m)
        fmt.Printf("Add tumblr source, %s: %s %s\n", m.Name, m.Suffix, m.Url)
    }
    return sources
}

