# 内容

此仓库为跟随[廖雪峰Python教程](https://liaoxuefeng.com/books/python/introduction/index.html)学习时编写的练习代码，章节为第10章：面向对象编程。

10. 面向对象编程
    1.  类和实例
    2.  访问限制
    3.  继承和多态

## 10.1 类和实例

类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

\>>> bart = Student('Bart Simpson', 59)
\>>> lisa = Student('Lisa Simpson', 87)
\>>> bart.age = 8
\>>> bart.age
8
\>>> lisa.age
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute 'age'

## 10.2 访问限制

## 10.3 继承和多态

继承可以把父类的所有功能都直接拿过来，这样就不必从零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。