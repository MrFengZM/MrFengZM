# with语句（上下文管理器）
# with 语句可以自动管理上下文资源，不论什么原有跳出with块，都能确保文件正确的关闭看，以此达到释放资源的目的
with open("1656861427454.jpg","rb") as file:
    with open("copy2@1656861427454.jpg","wb") as copy_file:
        copy_file.write(file.read())