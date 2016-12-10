package main

import "fmt"
import "net/http"
import "io/ioutil"

func main() {
    resp, err := http.Get("https://www.tiege.me/?p=802")
    if err != nil {
        fmt.Println(err)
    } else {

        b, err := ioutil.ReadAll(resp.Body)
        resp.Body.Close()
        if err != nil {
            fmt.Println(err)
        } else {
            fmt.Println(string(b))
        }
    }
}
