#### order by
**ASC**表示升序，**DESC**表示降序  
一般情况下，WHERE 用于过滤数据行，而 HAVING 用于过滤分组。  
WHERE 查询条件中不可以使用聚合函数，而 HAVING 查询条件中可以使用聚合函数。  
WHERE 在数据分组前进行过滤，而 HAVING 在数据分组后进行过滤 。  
WHERE 针对数据库文件进行过滤，而 HAVING 针对查询结果进行过滤。
也就是说，WHERE 根据数据表中的字段直接进行过滤，
而 HAVING 是根据前面已经查询出的字段进行过滤。  
WHERE 查询条件中不可以使用字段别名，而 HAVING 查询条件中可以使用字段别名。  

#### 自动化
python端: 运行脚本，并向移动设备发送HTTP请求  
移动设备：移动设备上运行了封装了uiautomator2的HTTP服务，解析收到的请求，
并转化成uiautomator2的代码。  

1. 在移动设备上安装atx-agent(守护进程), 随后atx-agent启动uiautomator2服务(默认7912端口)进行监听  
2. 在PC上编写测试脚本并执行（相当于发送HTTP请求到移动设备的server端）  
3. 移动设备通过WIFI或USB接收到PC上发来的HTTP请求，执行指定的操作  

**抓取手机上应用的控件**  
虽然很想用Android SDK内置工具uiautomatorviewer.bat，但是运行uiautomator2的时候，
uiautomatorviewer.bat运行不起来，两者之间冲突太严重。
于是参考着uiautomatorviewer的界面，我又写了一个weditor，
调用python-uiautomator2的两个接口screenshot和dump_hierarchy这样就不会有冲突问题了  


ResourceId定位: d(resourceId="com.smartisanos.clock:id/text_stopwatch").click()  
Text定位 d(text="秒表").click()  
Description定位 d(description="..").click()  
ClassName定位 d(className="android.widget.TextView").click()  


facebook-wda  

原理：对于iOS自动化操作，主要靠WebDriverAgent来完成。  
1. 在Mac电脑上连接真机iPhone，运行WebDriverAgentRunner会在Mac端启动WDA服务器，  
2. 在手机iPhone端安装一个WebDriverAgentRunner应用。  
3. 我们通过编写脚本来与WDA服务器通信，告诉WDA服务器我们想要如何操作iPhone手机，  
4. WDA服务器与安装在手机iPhone端的WebDriverAgentRunner应用通信并通过该app发送模拟指令来实现操作iPhone手机  


#### get element attributes  
e.className # XCUIElementTypeStaticText  
e.name # XCUIElementTypeStaticText  /name  
e.visible # True    /attribute/visible  
e.value # Dashboard /attribute/value  
e.label # Dashboard /attribute/label  
e.text # Dashboard  /text  
e.enabled # True    /enabled  
e.displayed # True  /displayed  


-- 创建SRS数据库  
drop database if exists SRS;  
create database SRS default charset utf8 collate utf8_bin;  

-- 切换到SRS数据库  
use SRS;  

-- 创建学院表  
create table tb_college
(
collid int not null auto_increment comment '学院编号',
collname varchar(50) not null comment '学院名称',
collmaster varchar(20) not null comment '院长姓名',
collweb varchar(511) default '' comment '学院网站',
primary key (collid)
);  

-- 添加唯一约束  
alter table tb_college add constraint uni_college_collname unique (collname);  

-- 创建学生表  
create table tb_student
(
stuid int not null comment '学号',
sname varchar(20) not null comment '学生姓名',
gender bit default 1 comment '性别',
birth date not null comment '出生日期',
addr varchar(255) default '' comment '籍贯',
collid int not null comment '所属学院编号',
primary key (stuid)
);  

-- 添加外键约束  
alter table tb_student add constraint fk_student_collid foreign key (collid) references tb_college (collid);  

-- 创建教师表  
create table tb_teacher
(
teaid int not null comment '教师工号',
tname varchar(20) not null comment '教师姓名',
title varchar(10) default '' comment '职称',
collid int not null comment '所属学院编号'
);  

-- 添加主键约束  
alter table tb_teacher add constraint pk_teacher primary key (teaid);  

-- 添加外键约束  
alter table tb_teacher add constraint fk_teacher_collid foreign key (collid) references tb_college (collid);  

-- 创建课程表  
create table tb_course
(
couid int not null comment '课程编号',
cname varchar(50) not null comment '课程名称',
credit tinyint not null comment '学分',
teaid int not null comment '教师工号',
primary key (couid)
);  

-- 添加外键约束  
alter table tb_course add constraint fk_course_tid foreign key (teaid) references tb_teacher (teaid);  

-- 创建学生选课表  
create table tb_score
(
scid int not null auto_increment comment '选课编号',
sid int not null comment '学号',
cid int not null comment '课程编号',
seldate date comment '选课时间日期',
mark decimal(4,1) comment '考试成绩',
primary key (scid)
);  

-- 添加外键约束  
alter table tb_score add constraint fk_score_sid foreign key (sid) references tb_student (stuid);  
alter table tb_score add constraint fk_score_cid foreign key (cid) references tb_course (couid);  


-- 插入学院数据  
insert into tb_college (collname, collmaster, collweb) values 
('计算机学院', '左冷禅', 'http://www.abc.com'),
('外国语学院', '岳不群', 'http://www.xyz.com'),
('经济管理学院', '风清扬', 'http://www.foo.com');  

-- 插入学生数据  
insert into tb_student (stuid, sname, gender, birth, addr, collid) values
(1001, '杨逍', 1, '1990-3-4', '四川成都', 1),
(1002, '任我行', 1, '1992-2-2', '湖南长沙', 1),
(1033, '王语嫣', 0, '1989-12-3', '四川成都', 1),
(1572, '岳不群', 1, '1993-7-19', '陕西咸阳', 1),
(1378, '纪嫣然', 0, '1995-8-12', '四川绵阳', 1),
(1954, '林平之', 1, '1994-9-20', '福建莆田', 1),
(2035, '东方不败', 1, '1988-6-30', null, 2),
(3011, '林震南', 1, '1985-12-12', '福建莆田', 3),
(3755, '项少龙', 1, '1993-1-25', null, 3),
(3923, '杨不悔', 0, '1985-4-17', '四川成都', 3);  

-- 插入老师数据  
insert into tb_teacher (teaid, tname, title, collid) values 
(1122, '张三丰', '教授', 1),
(1133, '宋远桥', '副教授', 1),
(1144, '杨逍', '副教授', 1),
(2255, '范遥', '副教授', 2),
(3366, '韦一笑', '讲师', 3);  

-- 插入课程数据  
insert into tb_course (couid, cname, credit, teaid) values 
(1111, 'Python程序设计', 3, 1122),
(2222, 'Web前端开发', 2, 1122),
(3333, '操作系统', 4, 1122),
(4444, '计算机网络', 2, 1133),
(5555, '编译原理', 4, 1144),
(6666, '算法和数据结构', 3, 1144),
(7777, '经贸法语', 3, 2255),
(8888, '成本会计', 2, 3366),
(9999, '审计学', 3, 3366);  

-- 插入选课数据  
insert into tb_score (sid, cid, seldate, mark) values 
(1001, 1111, '2017-09-01', 95),
(1001, 2222, '2017-09-01', 87.5),
(1001, 3333, '2017-09-01', 100),
(1001, 4444, '2018-09-03', null),
(1001, 6666, '2017-09-02', 100),
(1002, 1111, '2017-09-03', 65),
(1002, 5555, '2017-09-01', 42),
(1033, 1111, '2017-09-03', 92.5),
(1033, 4444, '2017-09-01', 78),
(1033, 5555, '2017-09-01', 82.5),
(1572, 1111, '2017-09-02', 78),
(1378, 1111, '2017-09-05', 82),
(1378, 7777, '2017-09-02', 65.5),
(2035, 7777, '2018-09-03', 88),
(2035, 9999, date(now()), null),
(3755, 1111, date(now()), null),
(3755, 8888, date(now()), null),
(3755, 9999, '2017-09-01', 92);  

#### 索引
索引是**关系型数据库**对某一列或者某几列的值进行预排序的**数据结构**，
通过使用索引，数据库系统可以**不必扫描整个表，而直接定位到符合条件的记录**  

#### delete、drop、truncate
drop：删除表，同时删除表结构、属性和索引
delete：通过where子句删除符合条件的行，不删除表结构、索引、属性
truncate：删除表所有数据，不需要使用where子句，不删除表结构、索引和属性
注意：对于有主外键约束的表，不能用truncate，而应该使用不带where子句的delete语句，
由于truncate不记录在日志中，不能够激活触发器  

#### HTTP协议
应用层协议，  

#### IP协议
网络层协议，主要解决网络路由与寻址问题  

#### UDP/TCP
UDP：用户数据报协议，不可靠，无连接，面向报文，尽量大努力的交付，无流量控制，无阻塞控制，传输效果高，支持一对一、一对多、多对一、多对多的交互通信，一般用于即时通信：qq聊天、在线视频，网络电话  

TCP：传输控制协议，提供可靠交付服务，面向连接，基于字节流，有流量控制，有阻塞控制，传输效率低，点对点交互通信，对效率要求低，对准确度要求高或者是要求有连接的场景：文件传输、发送接收邮件、远程登录  

#### 短连接
浏览器与服务器每进行一次HTTP操作，就建立一次连接，但任务结束就中断连接  

#### 长连接（keepalive connections）
http有一种叫做长连接的机制，可以传输数据后仍保持连接，当客户端需要再次获取数据，直接使用网络空闲下来的连接而无需再次握手  
Connection:keep-alive   
HTTP协议的长连接和短连接，实质上是TCP协议的长连接和短连接  

#### http状态码
400：无法解析此请求  
403：禁止访问  
404：找不到文件目录  
500：服务器内部错误  
502：web服务器作为网关或者代理服务器收到无法解析的请求  

使用301的场景：（一般是资源位置永久更改）永久移动  
1.域名到期不想续费（或者发现了更适合网站的域名），想换个域名。  
2.在搜索引擎的搜索结果中出现了不带www的域名，而带www的域名却没有收录，这个时候可以用301重定向来告诉搜索引擎我们目标的域名是哪一个。  
3.空间服务器不稳定，换空间的时候。  

使用302的场景：（一般是普通的重定向需求：临时跳转）  
1.未登录前先使用302重定向到登录页面,登录成功后再跳回到原来请求的页面  
2.有时候需要自动刷新页面，比如5秒后回到订单详细页面之类。  
3.有时系统进行升级或者切换某些功能时，需要临时更换地址。  
4.像微博之类的使用短域名，用户浏览后需要重定向到真实的地址之类。  
5.电脑端与移动端的转换  

#### c/s 和 b/s的区别
C/S **是双向的通讯**，建立连接后会一直保持连接，任何一方都可以随时向对方发送信息。
比如QQ客户端登录后，腾讯的服务器可以随时把新的消息发给客户端，客户端也可以随时向腾讯的服务器发送信息  

B/S **是「查询」式的通讯**，客户端向服务器查询一些信息，在服务器回应之后，(逻辑上)会立刻断开连接。
只有客户端向服务器查询时，服务器才能向客户端发送信息，服务器不能主动地向客户端发送信息。
比如通过浏览器访问网站时，只有当你访问一个网站时，网站才可以向你提供信息。
「访问」是一个瞬间的行为，当网页加载完成以后，网站就无法再发送额外的信息。  

简而言之，**C/S 是双向通讯，B/S 是一问一答**。有人可能想到一些反例，比如 Web QQ, 
事实上(根据我前一阵的试验) Web QQ 会通过「阻塞长连接」的方式获取新的聊天消息，
依然还是 B/S 的模式。当然现在也有 WebSocket, 可以在浏览器上实现 C/S 通讯，不过目前应用还不够广泛。  

#### 子网掩码
子网掩码：它是用来划分**子网的网段**和**遮掩部分IP地址**。换个说法就是：**它是用来划分IP地址中哪一部分是网络号，哪一部分是机器号**，
子网掩码还需要满足一个条件才可以使用：它的二进制中1和0必须是连续的  
那子网掩码怎么用？  
答：用乘法来遮掩IP地址。1×1=1、1×0=0、0×0=0、0×1=0
1100 0000.1010 1000.0000 0001.0000 0000的十进制：192.168.1.0也就是说，从192.168.1.0到192.168.1.255都是同一个子网网段，里面的0—255号可以分配给不同的机器。
0—255号都是机器的号码，IP地址显示的就是其中129号。
192.168.1.0就是所谓的网络号，也可以写作192.168.1或者192.168.1.0\24（24指的是IP地址中有24位未被遮掩）  
总结：子网掩码就是用来遮掩IP地址并划分网段的工具，根据**遮掩的位数不同**来划分不同的网段  

#### python装饰器
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象  

#### python进程、线程、协程
1. **进程是一个实体**。每个进程都有自己的地址空间(CPU分配)。实体空间包括三部分：  
* 文本区域：存储处理器执行的代码。  
* 数据区域：存储变量或进程执行期间使用的动态分配的内存。  
* 堆栈：进程执行时调用的指令和本地变量。  
**进程的特点**  
* 动态性：进程是程序的一次执行过程，动态产生，动态消亡。  
* 独立性：进程是一个能独立运行的基本单元。是系统分配资源与调度的基本单元。  
* 并发性：任何进程都可以与其他进程并发执行  
2. **线程是进程中的一个实体**，是被系统独立调度和分派的基本单位。 线程的实体包括程序，数据，TCB。TCB包括：  
* 线程状态  
* 线程不运行时，被保存的现场资源  
* 一组执行堆栈  
* 每个线程的局部变量  
* 访问统一进程中的资源  
> * 线程自己不拥有系统资源，只拥有一点运行中必不可少的资源。* 同一进程中的多个线程并发执行，这些线程共享进程所拥有的资源。  
**进程与线程的区别**  
* 进程是CPU资源分配的基本单位，线程是独立运行和独立调度的基本单位（CPU上真正运行的是线程）。  
* 进程拥有自己的资源空间，一个进程包含若干个线程，线程与CPU资源分配无关，多个线程共享同一进程内的资源。  
* 线程的调度与切换比进程快很多。  
**协程是一种比线程更加轻量级的存在**，最重要的是，协程不被操作系统内核管理，协程是完全由程序控制的。  
运行效率极高，协程的切换完全由程序控制，不像线程切换需要花费操作系统的开销,线程数量越多，协程的优势就越明显。  
协程不需要多线程的锁机制，因为只有一个线程，不存在变量冲突。  
对于多核CPU，利用多进程+协程的方式，能充分利用CPU，获得极高的性能。  

#### 生成器和迭代器
迭代器：它是一个带状态的对象，它能在你调用next()方法的时候返回容器中的下一个值，任何实现了__iter__()和__next__()方法的对象都是迭代器，__iter__返回迭代器自身，__next__返回容器中的下一个值，如果容器中没有更多元素了，则抛出Stop Iteration异常。  
生成器：在Python中，使用了yield的函数被称为生成器（generator），跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个特殊的迭代器，调用一个生成器函数，返回的是一个迭代器对象。它不需要再像上面的类一样写__iter__()和__next__()方法了，只需要一个yiled关键字，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值,并在下一次执行next()方法时从当前位置继续运行（这也是生成器的主要使用场景）。  

集合时无序的，因此也没有索引，要访问元素，有两种方法：  
1. 转换为列表，list()
2. 转换为迭代器，iter()

迭代器的应用：  
不需要事先准备好整个迭代过程中的所有元素，迭代器仅仅在迭代到某个元素时才计算该元素，应用于遍历一些巨大的或者无限的集合  

### python
1. sort() ：仅对list对象进行排序，会改变list自身的顺序，没有返回值，即原地排序；  
2. sorted() ：对所有可迭代对象进行排序，返回排序后的新对象，原对象保持不变；  


### linux
1. find命令
find是搜索文件名，查找匹配条件的文件，输出匹配文件  
```shell
命令格式：find -name '要查找的文件名' | xargs perl -pi -e 's|被替换的字符串|替换后的字符串|g' 

#### 查找替换当前目录下包含字符串并进行替换

find -name '*.txt' | xargs perl -pi -e 's|智慧乡村|北部山区|g'

#### 递归查找替换

find . -type f -name '*.html' | xargs perl -pi -e 's|智慧乡村|北部山区|g'
```
2. grep
是搜索文件内容，查找匹配条件的文件行，输出匹配行或含有匹配内容的文件  
```shell
格式: sed -i "s/查找字段/替换字段/g" `grep 查找字段 -rl 路径`  
sed -i "s/www.admin99.net/admin99.net/g" `grep www.admin99.net -rl /home`    #替换/home下所有文件中的www.admin99.net为admin99.net
```
3. tar
压缩文件
```shell
tar -zcvf xx.tar.gz
其中：
    z: 调用gzip压缩命令进行压缩
    c: 打包文件
    v: 显示运行进程
    f: 指定文件名
```
解压缩文件
```shell
tar -xvf xxx.tar.gz
其中：
    x: 代表解压
tar -xvf xxx.tar.gz -C /usr
其中，C代表指定解压的位置，而且是大写
```



### vim
1. 查找模式
一般模式下，点击/进入查找模式, \c表示大小写不敏感
```shell
/foo\c
```
2. 查找和替换
:s(substitute)命令用来查找和替换字符串
:{作用范围}s/{目标}/{替换}/{替换标志}
- 当前行
```shell
:s/foo/bar/g
```
- 全文
```shell
:%s/foo/bar/g
```
- 指定行数 2-11
```shell
:2, 12s/foo/bar/g
```
vim快速定位到最后一行和最后一行的最后一个字符
```shell
按G，即shift+g --- 最后一行
按G，先定位到最后一行，再按$即shift+4 --- 最后一行的最后一个字符
```
































1.查询"01"课程比"02"课程成绩高的学生的信息及课程分数  
```mysql
select stu.*, t1.mark, t2.mark from tb_student stu join tb_score t1 on stu.stuid=t1.sid 
and t1.cid='1111' join tb_score t2 on stu.stuid=t2.sid 
and t2.cid='2222' where t1.mark>t2.mark;
```
```mysql
select * from (select sid, mark from tb_score where cid='1111') t1, 
(select sid, mark from tb_score where cid='2222' ) t2 where 
t1.mark>t2.mark and t1.sid=t2.sid;
```
```mysql
select stu.*, t1.mark, t2.mark 
from tb_student stu, tb_score t1, tb_score t2 
where stu.stuid=t1.sid and stu.stuid=t2.sid and t1.cid='1111' 
and t2.cid='2222' and t1.mark>t2.mark;
```


































































































































