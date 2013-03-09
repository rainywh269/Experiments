package downloader
import (
    "time"
    "net"
    )

func timeoutDialler(ns int64) func(net, addr string) (c net.Conn, err error) {
    return func(netw, addr string) (net.Conn, error) {
        c, err := net.Dial(netw, addr)
        if err != nil {
            return nil, err
        }
        c.SetDeadline(time.Now().Add(time.Duration(ns) * time.Second))
        return c, nil
    }
}
