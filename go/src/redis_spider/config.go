package main

import "time"

const REDIS_NETWORK = "unix"
const REDIS_LOCATION = "/tmp/redis.sock"
const CONCURENT_DOWNLOADS = 4

const HTTP_PROXY = "http://10.8.0.1:8118"
const CHECK_INTERVAL = time.Minute * 1
const SET_NAME = "url_set"
