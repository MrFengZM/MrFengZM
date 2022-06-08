# r 打开模式 以只读的模式打开文件 文件的指针将会放在文件的开头
# w 以只写的模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容
# a 以追加的模式打开文件如果文件不存在则创建，文件指针在文件开头
# b 以二进制方式打开文件，不能单独使用，需要与其他模式一起使用，rb，或wb
# + 以读写方式打开文件，不能单独使用，需要与其他模式一起使用，a+
import pytest

def test_open_r():
    # r 打开模式 以只读的模式打开文件 文件的指针将会放在文件的开头
    file=open('sql.sql','r') # 以只读模式打开
    print(file.readlines()) # 打印文件内容(列表形式)
    file.close()  # 关闭文件


def test_open_w():
    # w 以只写的模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容
    file = open("sql.sql","w") # 以只写模式打开
    file.write("select") # 覆盖重写原文件
    file.close()


def test_open_a():
    # a 以追加的模式打开文件如果文件不存在则创建，文件指针在文件开头
    file=open("sql.sql","a") # 以追加模式打开文件
    file.write("from where order by limit") # 在原有文件后面追加写入
    file.close()


def test_open_b():
    # b 以二进制方式打开文件，不能单独使用，需要与其他模式一起使用，rb，或wb
    file=open("1656861427454.jpg","rb")
    wb_file=open("copy1656861427454.jpg","wb")
    wb_file.write(file.read())  # 复制已读的文件到新的文件
    file.close()
    wb_file.close()


def  test_open_jia():
    # + 以读写方式打开文件，不能单独使用，需要与其他模式一起使用，a+
    file = open("test_git.py","r+")
    print("hahahahhahahaha",file.readlines())
    file.write(f"hahahah{file.read()}")
    file.close()








file=open('sql.sql','r')
