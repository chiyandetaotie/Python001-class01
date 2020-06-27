1、python官方文档：
	https://docs.python.org/zh-cn/3.7/ 


2、git的安装使用： 
	初始化本地仓库：git init 
	配置用户名邮箱：git config --global user.name "username" git config --global user.email "email"
	跟踪文件命令：git add . 
	提交文件命令：git commit -m '注释说明' 查看历史提交状态：git log
	fork;复制仓库 
	clone 克隆到本地 ： git clone git@github.com:xiaofengxue/Python001-class01.git 
	上传到 github： git push -u origin master 
	作业提交链接：https://github.com/Python001-class01/Python001-class01/issues/1


3、requests 两个方法： 
	post 发送请求 
	get 获取响应内容 


4、Beautiful Soup 
	官方文档链接： https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/ 
	find_all('div',attrs={'class':'movie-item-hover'}) : 查找div标签下class属性为：'movie-item-hover对应的内容 
	get_text() 获取文本内容 


5、Scrapy

	安装 scrapy ：pip install scrapy
	框架解析 ：
		   Scapy Engine(配置域名)-->Spider Midlewares-->Spiders(爬虫器，解析网页[BeautifulSoup库]，需要自己编写)
		-->Scapy Engine-->Scheduler(调度器，用来去重)
		-->Scapy Engine-->Downloader Midlewares--> Downloader(下载器，获取网页[requessts库])
		-->Scapy Engine-->Spider Midlewares-->Spiders(爬虫解析器) 
		-->Scapy Engine|-->Scheduler
		               |
                               | -->Item Pipeline(管道，存储数据[保存到csv、txt、MySQL中]，需要自己编写)

	建立项目：
	scrapy startproject spiders
	cd spiders
	cd spiders
	scrapy genspider movies douban.com



	运行代码：
	scrapy crawl douban


6、 Xpath 
	官方学习文档： https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths Xpath 
	中文文档： https://www.w3school.com.cn/xpath/index.asp Xpath 
	英文文档： https://www.w3.org/TR/2017/REC-xpath-31-20170321/#nt-bnf 
	xpath('//div[@class="movie-hover-info"]') // 灵活匹配 ./ 下一级目录寻找 ../ 同级目录寻找 /text() 获取文本内容 /@href 获取属性内容


