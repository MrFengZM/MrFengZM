import logging


def menun():

    print(f"{'='*20}<学生信息管理系统>{'='*20}\n")
    print(f"{'—'*20}<功能菜单>{'—'*20}\n")
    print('\t\t\t1.录入学生信息')
    print('\t\t\t2.查找学生信息')
    print('\t\t\t3.删除学生信息')
    print('\t\t\t4.修改学生信息')
    print('\t\t\t5.排序')
    print('\t\t\t6.统计学生总人数')
    print('\t\t\t7.显示所有学生信息')
    print('\t\t\t0.退出')
    print("—————————————————————————"*2)

def main():
    while True:
        menun()
        choice = int(input("请选择"))
        if choice in (0,1,2,3,4,5,6,7):
            if choice == 0:
                result=input("您确定退出系统？（y/n）")
                if result == "y":
                    print("退出程序")
                    break
                else:
                    print("返回菜单")
                    continue

            elif choice == 1:
                insert()
                pass
            elif choice == 2:
                search()
                pass
            elif choice == 3:
                delete()
                pass
            elif choice == 4:
                modify()
                pass
            elif choice == 5:
                sort()
                pass
            elif choice == 6:
                total()
            elif choice == 7:
                show()


        else:
            logging.exception("选择错误")

def insert():
    student_list = []
    while True:
        id = input("请输入id")
        if not id : break
        name = input("请输入姓名")
        if not name : break
        try:
            python = input("请输入python成绩")
            java = input("请输入java成绩")
            english = input("请输入英语成绩")
        except Exception as log:
            print(log)
        else:
            student = {"id":id,"name":name,"python":python,"java":java,"英语":english}  # 学生信息
            student_list.append(student)  # 存入列表
            result = input("是否继续输入（y/n）")
            if result is "y" :continue
            else:break

    save(student_list)

def search():
    pass

def delete():
    pass

def modify():
    pass

def sort():
    pass

def total():
    pass

def show():
    pass


def save(student_list):
    with open("student.txt","a+",encoding="utf-8") as file:
        for i in student_list:
            file.write(str(i)+"\n")





main()

