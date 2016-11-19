package org.dataforum.sqlite;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import org.sqlite.JDBC;

public class Sqlite {
	//主函数
		public static void main(String[] args) {
			// TODO Auto-generated method stub
			try{
				Sqlite sqlite = new Sqlite();
			    String sql="select id,name,email from users";
			    ResultSet rs = sqlite.select(sql);
			    while(rs.next()){
					System.out.println("ID号："+rs.getString(1)+"\n"+"用户名："+rs.getString(2)+"\n"+"邮箱："+rs.getString(3));
			    }
			}catch (Exception e){
				e.printStackTrace();;
			}
		}
		
		// 声明数据库地址及驱动
		private Connection conn = null;
		private String url = "jdbc:sqlite:";
		private String driver = "org.sqlite.JDBC";
		private String fileName = "/home/abelit/workspace/ConnectDatabase/sqlite/abelit.db";

		// 创建数据库连接方法
		public Connection create() {
			try {
				/* 使用Class.forName()方法自动创建这个驱动程序的实例且自动调用DriverManager来注册它 */
				Class.forName(driver);
				/* 通过DriverManager的getConnection()方法获取数据库连接 */
				conn = DriverManager.getConnection(url+fileName);
			} catch (Exception ex) {
				System.out.println("数据库连接出错");
			}
			return conn;
		}

		// 执行查询时用的方法
		public ResultSet select(String sql) {
			Connection conn = create();//获取连接对象,可以不声明
			ResultSet rs = null;
			try {
				Statement st = conn.createStatement();// 获取Staetment对象
				rs = st.executeQuery(sql);// 执行操作
			} catch (Exception e) {
				System.out.println("查询出错");
			} finally{
				//conn.close();
			}
			return rs;
		}

		// 更新方法
		public void execute(String sql) {
			Connection conn = create();//获取连接对象,可以不声明
			ResultSet rs = null;
			try {
				Statement st = conn.createStatement();// 获取Staetment对象
				st.executeUpdate(sql);
			} catch (Exception e) {
				System.out.println("更新出错");
			}

		}
}
