package main

import "net/http"

func main() {
	http.HandleFunc("/", someFunc)
	http.ListenAndServe(":8080", nil)
}

func someFunc(w http.ResponseWriter, req *http.Request) {
	w.Write([]byte("Welcome to website built by go lang, Abelit! "))
}
