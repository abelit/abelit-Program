package main

import "github.com/go-martini/martini"

func listBook(book string) string {
    return "<h1>Book List</h1> <li>%s</li>" 
}

func main() {
  m := martini.Classic()
  m.Get("/", func() string {
    return "Hello world!"
  })
  m.Get("/name", func() string {
    return "Welcome to martini webpage, Abelit!"
  })

  m.Get("/books", func() string {
    
  })

  m.Run()
}
