package org.dataforum.mongodb;

import com.mongodb.MongoClient;
import com.mongodb.client.MongoDatabase;

public class Mongodb {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			// 连接到 mongodb 服务
			// 实例化Mongo对象，连接27017端口  
            MongoClient mongoClient = new MongoClient("localhost");  

			// 连接到数据库
			MongoDatabase mongoDatabase = mongoClient.getDatabase("mycol");
			System.out.println("Connect to database successfully");
			

		} catch (Exception e) {
			System.err.println(e.getClass().getName() + ": " + e.getMessage());
		    e.printStackTrace();
		}
	}

}