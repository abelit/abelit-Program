package controllers

import (
	"github.com/astaxie/beego"
)

type HomeController struct {
	beego.Controller
}

func (c *HomeController) Get() {
	c.Data["name"] = "Abelit"
	c.Data["website"] = "www.dataforum.org"
	c.Data["email"] = "ychenid@live.com"
	c.TplName = "home.tpl"
}
