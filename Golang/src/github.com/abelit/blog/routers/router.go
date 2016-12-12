package routers

import (
	"github.com/abelit/blog/controllers"
	"github.com/astaxie/beego"
)

func init() {
    beego.Router("/", &controllers.MainController{})
	beego.Router("/home", &controllers.HomeController{})
}
