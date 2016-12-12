package controllers

import (
	"github.com/astaxie/beego"
)

type MainController struct {
	beego.Controller
}

// type HomeController struct {
// 	beego.Controller
// }

func (c *MainController) Get() {
	c.Data["Website"] = "beego.me"
	c.Data["Email"] = "astaxie@gmail.com"
	c.TplName = "index.tpl"
}

// func (c *HomeController) Get() {
// 	c.Data["name"] = "Abelit"
// 	c.Data["website"] = "www.dataforum.org"
// 	c.Data["email"] = "ychenid@live.com"
// 	c.TplName = "home.tpl"
// }
