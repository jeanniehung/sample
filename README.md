# sample
sample

在for循环中还有很多有用的东西，如下：

变量	                描述
forloop.counter	        索引从 1 开始算
forloop.counter0	    索引从 0 开始算
forloop.revcounter	    索引从最大长度到 1
forloop.revcounter0	    索引从最大长度到 0
forloop.first	        当遍历的元素为第一项时为真
forloop.last	        当遍历的元素为最后一项时为真
forloop.parentloop	    用在嵌套的 for 循环中，获取上一层 for 循环的 forloop

当列表中可能为空值时用 for  empty
{% for i in EmptyList %}
    {{i}}
{% empty %}
    {{'Empty'}}
{% endfor %}

还可以使用 as 语句将内容取别名（相当于定义一个变量），多次使用（但视图名称到网址转换只进行了一次）

与数据库关联

