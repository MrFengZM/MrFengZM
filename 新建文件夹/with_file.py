
with open("1656861427454.jpg","rb") as file:
    with open("copy2@1656861427454.jpg","wb") as copy_file:
        copy_file.write(file.read())