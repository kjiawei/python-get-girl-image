## 项目说明
本项目是基于python3 django2.0.3的电商网站
需求文档见上级目录/电商网站需求
定位:生鲜品类电子商务网站 乐智商城
username:admin  password:kjw123456  (设置的密码保存到哪)

### 文件说明
manage.py：一个命令行工具，可以使你用多种方式对Django项目进行交互。 你可以在django-admin和manage.py中读到关于manage.py的所有细节。
内层的mysite/目录是你的项目的真正的Python包。它是你导入任何东西时将需要使用的Python包的名字（例如 mysite.urls）。
mysite/__init__.py：一个空文件，它告诉Python这个目录应该被看做一个Python包。 （如果你是一个Python初学者，关于包的更多内容请阅读Python的官方文档）。
mysite/settings.py：该Django 项目的设置/配置。Django 设置 将告诉你这些设置如何工作。
mysite/urls.py：该Django项目的URL声明；你的Django站点的“目录”。 你可以在URL 转发器 中阅读到更多关于URL的内容。
mysite/wsgi.py：用于你的项目的与WSGI兼容的Web服务器入口;

### 开发进度  11.15看到第3部分新手教程出错了
方式:测试/数据驱动开发
开发环境:
官方教程  https://yiyibooks.cn/xx/django_182/intro/tutorial01.html
里面有很多模块例子 https://zhuanlan.zhihu.com/djstudyteam
Django项目与Django应用的关系及django.apps模块 https://blog.csdn.net/taiyangdao/article/details/78105548
https://www.zmrenwu.com/post/2/
极客学院视图与路由(正则表达式)  http://www.jikexueyuan.com/course/1325_1.html?ss=1
python项目列表 http://www.ibeifeng.cn/page/job_python.html?hmsr=cn-bdss&hmmd=cpc&hmpl=pb318-python&hmcu=mk001-python&hmkw=53805877704_django%E8%A7%86%E9%A2%91%E6%95%99%E7%A8%8B&hmci=13609129865&matchtype=1&adposition=cl5&pagenum=1&matchtype=1&adposition=cl5&pagenum=1&e_keywordid=53805877704#python-prg
*pycharm如何新建django项目


常见错误
1.indent 需要将所有空格转tab
7.更改setting时区会出现 if zone.upper()=='UTC'  nonetype object has no attribute 'upper'
8.url视图路径出错  https://www.cnblogs.com/way_testlife/archive/2011/03/22/1991453.html  解决了

常用命令
查看Django版本号
1.python -m django --version
- import django
- print(django.get_version())

新建django项目 : python django-admin.py startproject projectName

(修改INSTALLED_APPS后更新及修改数据表python manage.py makemigrations polls ; [python manage.py sqlmigrate polls 0001;] py -3 manage.py migrate;) 解决python2共存创建数据表问题
模型更新 python manage.py makemigrations polls
