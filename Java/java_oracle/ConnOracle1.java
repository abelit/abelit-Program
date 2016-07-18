package com.chenying;
import java.sql.*;

//使用jdbc.odbc连接数据库
public class TestOra {
	public static void main (String[] args) {

		try {
			//加载驱动
			//注意，jdbc.odbc不能进行远程连接

			Class.forName("sun.jdbc.odbc.JdbcOdbcDriver");

			//得到链接
			Connection ct=DriverManager.getConnection("jdbc:odbc:testchenying","c##scott","tiger");
			
			Statement sm=ct.createStatement();

			ResultSet rs=sm.executeQuery("select * from emp");
			while(rs.next()){
				System.out.println("用户名："+rs.getString(2));
			}

			//关闭打开的资源
			rs.close();
			sm.close();
			ct.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}