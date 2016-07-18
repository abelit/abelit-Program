package com.chenying;
import java.sql.*;

//使用jdbc连接数据库
public class TestOra2 {
	public static void main (String[] args) {

		try {
			//加载驱动
			//注意，jdbc.odbc不能进行远程连接

			Class.forName("oracle.jdbc.driver.OracleDriver");

			//连接oracle
			Connection ct=DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:orcl","c##scott","tiger");
			
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