package main
 
import (
    "database/sql"
    "fmt"
    _ "github.com/go-sql-driver/mysql"
)
 
type userinfo struct {
    name    string
    email  string
}
 
func main() {
    // db, err := sql.Open("mysql", "root:cy123@tcp(127.0.0.1:3306)/dataforum?charset=utf8")
    db, err := sql.Open("mysql", "root:cy123@/dataforum?charset=utf8")
    checkErr(err)
    rows, err := db.Query("SELECT name,email FROM users")
    checkErr(err)
    for rows.Next() {
        var name,email string
        if err := rows.Scan(&name, &email); err == nil {
            fmt.Println(err)
        }
        fmt.Println(name)
        fmt.Println(email)
    }
}
 
func checkErr(err error) {
    if err != nil {
        panic(err)
    } else {
            fmt.Println("No error found!")
    }
}
