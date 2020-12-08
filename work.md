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
3. 移动设备通过WIFI或USB接收到PC上发来的HTTP请求，执行制定的操作  

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

#### UDP/TCP
UDP：用户数据报协议，不可靠，无连接，面向报文，尽量大努力的交付，无流量控制，无阻塞控制，传输效果高，支持一对一、一对多、多对一、多对多的交互通信，一般用于即时通信：qq聊天、在线视频，网络电话

TCP：传输控制协议，提供可靠交付服务，面向连接，面向字节流，有流量控制，有阻塞控制，传输效率低，点对点交互通信，对效率要求低，对准确度要求高或者是要求有连接的场景：文件传输、发送接收邮件、远程登录

#### 长连接（keepalive connections）
http有一种叫做长连接的机制，可以传输数据后仍保持连接，当客户端需要再次获取数据，直接使用网络空闲下来的连接而无需再次握手  

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
C/S **是双向的通讯**，建立连接后会一直保持链接，任何一方都可以随时向对方发送信息。
比如QQ客户端登录后，腾讯的服务器可以随时把新的消息发给客户端，客户端也可以随时向腾讯的服务器发送信息  

B/S **是「查询」式的通讯**，客户端向服务器查询一些信息，在服务器回应之后，(逻辑上)会立刻断开连接。
只有客户端向服务器查询时，服务器才能向客户端发送信息，服务器不能主动地向客户端发送信息。
比如通过浏览器访问网站时，只有当你访问一个网站时，网站才可以向你提供信息。
「访问」是一个瞬间的行为，当网页加载完成以后，网站就无法再发送额外的信息。  

简而言之，**C/S 是双向通讯，B/S 是一问一答**。有人可能想到一些反例，比如 Web QQ, 
事实上(根据我前一阵的试验) Web QQ 会通过「阻塞长连接」的方式获取新的聊天消息，
依然还是 B/S 的模式。当然现在也有 WebSocket, 可以在浏览器上实现 C/S 通讯，不过目前应用还不够广泛。  

#### 子网掩码
子网掩码：它是用来划分**子网的网段**和**遮掩部分IP地址**。换个说法就是：**它是用来划分IP地址中哪一部分是网络号，哪一部分是机器号**
子网掩码还需要满足一个条件才可以使用：它的二进制中1和0必须是连续的  
那子网掩码怎么用？  
答：用乘法来遮掩IP地址。1×1=1、1×0=0、0×0=0、0×1=0
1100 0000.1010 1000.0000 0001.0000 0000的十进制：192.168.1.0也就是说，从192.168.1.0到192.168.1.255都是同一个子网网段，里面的0—255号可以分配给不同的机器。
0—255号都是机器的号码，IP地址显示的就是其中129号。
192.168.1.0就是所谓的网络号，也可以写作192.168.1或者192.168.1.0\24（24指的是IP地址中有24位未被遮掩）  
总结：子网掩码就是用来遮掩IP地址并划分网段的工具，根据**遮掩的位数不同**来划分不同的网段  

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


































































































































