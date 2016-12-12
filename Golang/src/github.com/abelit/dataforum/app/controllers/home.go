package controllers

import "github.com/revel/revel"

type Home struct {
	*revel.Controller
}

type User struct {
    name string
    email string
    age int
}

func (c Home) Index() revel.Result {
	// name := "Abelit"
	// email := "ychenid@live.com"
    // age := 27
    data := &User{"Abelit", "ychenid@gmail.com", 27}
	return c.Render(data)
}
