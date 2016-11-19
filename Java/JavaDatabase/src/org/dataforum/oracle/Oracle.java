package org.dataforum.oracle;

import java.sql.*;

public class Oracle {
	//主函数
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try{
			Oracle oracle = new Oracle();
		    String sql="select instance_name,host_name from gv$instance";
		    ResultSet rs = oracle.select(sql);
		    while(rs.next()){
				System.out.println("实例名："+rs.getString(1)+"\t\t"+"主机名："+rs.getString(2));
		    }
		}catch (Exception e){
			e.printStackTrace();;
		}
	}
	
	// 声明数据库地址及驱动
	private Connection conn = null;
	private String url = "jdbc:oracle:thin:@172.28.1.221:1521:gzgszxk1";
	private String driver = "oracle.jdbc.driver.OracleDriver";
	private String user = "sys as sysdba";
	private String password = "dba1d71f678513c02d0";

	// 创建数据库连接方法
	public Connection create() {
		try {
			/* 使用Class.forName()方法自动创建这个驱动程序的实例且自动调用DriverManager来注册它 */
			Class.forName(driver);
			/* 通过DriverManager的getConnection()方法获取数据库连接 */
			conn = DriverManager.getConnection(url, user, password);
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
