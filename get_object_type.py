# 获取对象信息
from animals import Animal

# 通过 type() 判断对象类型
# 基本类型都可以使用 type() 判断
print(type(123))
print(type("hello"))
print(type(None))

# 指向函数或类的变量，也可以用 type() 判断
print(type(abs))

ani = Animal()
print(type(ani))

