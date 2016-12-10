package main
 
import (
    "database/sql"
    "fmt"
    _ "github.com/go-sql-driver/mysql"
)
 
func main() {
    query()
}
 
//插入demo
func insert() {
    db, err := sql.Open("mysql", "root:cy123@/dataforum?charset=utf8")
    checkErr(err)
    stmt, err := db.Prepare(`INSERT users (name,email,password) values (?,?,?)`)
    checkErr(err)
    res, err := stmt.Exec("tony", "ychenid@gmail.com", "cy123")
    checkErr(err)
    id, err := res.LastInsertId()
    checkErr(err)
    fmt.Println(id)
}
 
//查询demo
func query() {
    db, err := sql.Open("mysql", "root:cy123@/dataforum?charset=utf8")
    checkErr(err)
 
    rows, err := db.Query("SELECT * FROM user")
    checkErr(err)
    //字典类型
    //构造scanArgs、values两个数组，scanArgs的每个值指向values相应值的地址
    columns, _ := rows.Columns()
    scanArgs := make([]interface{}, len(columns))
    values := make([]interface{}, len(columns))
    for i := range values {
        scanArgs[i] = &values[i]
    }
 
    for rows.Next() {
        //将行数据保存到record字典
        err = rows.Scan(scanArgs...)
        record := make(map[string]string)
        for i, col := range values {
            if col != nil {
                record[columns[i]] = string(col.([]byte))
            }
        }
        fmt.Println(record)
    }
}
 
//更新数据
func update() {
    db, err := sql.Open("mysql", "root:cy123@/dataforum?charset=utf8")
    checkErr(err)
 
    stmt, err := db.Prepare(`UPDATE user SET user_age=?,user_sex=? WHERE user_id=?`)
    checkErr(err)
    res, err := stmt.Exec(21, 2, 1)
    checkErr(err)
    num, err := res.RowsAffected()
    checkErr(err)
    fmt.Println(num)
}
 
//删除数据
func delete() {
    db, err := sql.Open("mysql", "root:cy123@/dataforum?charset=utf8")
    checkErr(err)
 
    stmt, err := db.Prepare(`DELETE FROM users WHERE id=?`)
    checkErr(err)
    res, err := stmt.Exec(1)
    checkErr(err)
    num, err := res.RowsAffected()
    checkErr(err)
    fmt.Println(num)
}
 
func checkErr(err error) {
    if err != nil {
        panic(err)
    }
}