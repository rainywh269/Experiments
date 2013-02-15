package redis

import (
	"testing"
)

func TestSet(t *testing.T) {
    test_set := "test_set"
    test_value_single_int := 1
    test_value_string := "http://24.media.tumblr.com/tumblr_me172lpP3G1qzpjbfo1_1280.jpg"
    test_value_string_not := "string2"

    conn := Redis{Network:"tcp", Location: ":6379"}
    conn.Connect()
    defer conn.Close()

    conn.Sadd(test_set, test_value_single_int)
    conn.Sadd(test_set, test_value_string)
    
    var is_in bool
    is_in = conn.Sismember(test_set, test_value_single_int)
    if !is_in{
        t.Error("ERR")
    }
    is_in = conn.Sismember(test_set, test_value_string)
    if !is_in{
        t.Error("ERR")
    }
    is_in = conn.Sismember(test_set, test_value_string_not)
    if is_in{
        t.Error("ERR")
    }
}
