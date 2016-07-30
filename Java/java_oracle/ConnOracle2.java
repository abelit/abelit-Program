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
			Connection ct=DriverManager.getConnection("jdbc:oracle:thin:@172.28.1.222:1521:gzgszxk","abelit","cy123");
			
			Statement sm=ct.createStatement();

			ResultSet rs=sm.executeQuery("select * from a_bm_xzqh");
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
