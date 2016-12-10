package main

import "fmt"

type Books struct {
	title string
	author string
	subject string
	book_id int
}

func main() {
	// 声明 Book1 Book2为 Books 类型
	var Book1 Books 
	var Book2 Books


	Book1.title = "Go Lang"
	Book1.author = "Abelit"
	Book1.subject = "Learn go lang"
	Book1.book_id = 520121001

	Book2.title = "Python"
	Book2.author = "Abelit"
	Book2.subject = "Learn Python"
	Book2.book_id = 520121002

	fmt.Printf( "Book 1 title : %s\n", Book1.title)
	fmt.Printf( "Book 1 author : %s\n", Book1.author)
	fmt.Printf( "Book 1 subject : %s\n", Book1.subject)
	fmt.Printf( "Book 1 book_id : %d\n", Book1.book_id)

	/* 打印 Book2 信息 */
	fmt.Printf( "Book 2 title : %s\n", Book2.title)
	fmt.Printf( "Book 2 author : %s\n", Book2.author)
	fmt.Printf( "Book 2 subject : %s\n", Book2.subject)
	fmt.Printf( "Book 2 book_id : %d\n", Book2.book_id)
}
