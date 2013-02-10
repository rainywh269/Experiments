package main

type Recorder interface {
    MarkAsFinished(url string)
    HasFinished(url string) bool
}
