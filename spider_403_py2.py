	# _*_ coding:utf-8 _*_
	#!/usr/bin/env python
	
	import urllib2 
	import random
	
	url = "http://blog.csdn.net/happydeer"
	agentHeaders= [
	        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
	        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0",
	        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
	        ]
	def getContent(url,Headers):
	        """
	        抓取浏览器能正常访问，但是使用爬虫返回403的页面
	        """
	        random_header = random.choice(Headers)
	
	        req = urllib2.Request(url)
	        req.add_header("User-Agent",random_header)  #这些数据通过‘查看元素’->‘网络’获得
	        req.add_header("Host","blog.csdn.net")
	        req.add_header("Referer","http://blog.csdn.net/")
	        req.add_header("GET",url)
	
	        content=urllib2.urlopen(req).read()
	        return content
	
	print getContent(url,agentHeaders)
