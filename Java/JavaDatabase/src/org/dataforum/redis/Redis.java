package org.dataforum.redis;

import redis.clients.jedis.Jedis;

public class Redis {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//连接Redis服务器，localhost：6379
		Jedis jedis = new Jedis("localhost",6379);
		System.out.println("Connect to redis successfully!");
		
		//测试连接Redis服务器是否成功
		System.out.println("Jedis pings: "+jedis.ping());
		
		//添加数据
		jedis.set("name", "lipanpan");
		jedis.append("name", " is my lover!");
		//查询数据
		String jrs = jedis.get("name");
		System.out.println(jrs);
	}

}
