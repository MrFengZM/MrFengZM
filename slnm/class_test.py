
class Person(object):
    def __init__(self):
        self.__age = 18  # 定义一个私有化属性，属性名字前加连个 __ 下滑线

    @property
    def age(self):  # 访问私有实例属性
        return self.__age

    @age.setter
    def age(self, age):  # 修改私有实例属性
        if age < 0:
            print('年龄不能小于0')
        else:
            self.__age = age





    # age = property(qet_age, et_age)  # 定义一个属性，当对这个age设置值时调用set_age,
# 当获取值时调用get_age
# 注意：必须是以get,set开头的方法名，才能被调用
xiaoming = Person()
xiaoming.age = 15
print(xiaoming.__dict__) # 内置属性 打印所有类属性

