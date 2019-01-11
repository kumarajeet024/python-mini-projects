import os
def rename():
    #get files name from a folder
    file_list = os.listdir(r"C:\Users\Ajeet\Desktop\python_mini_projects\prank\prank")
    # r is used to take to given path as raw format
    print(file_list)
    current_path = os.getcwd()
    #os.getcwd is used to know the current working directory

    os.chdir(r"C:\Users\Ajeet\Desktop\python_mini_projects\prank\prank")
    #os.chdir is used to change the current working directory
    print("current working directory is " + current_path)
    table = str.maketrans(dict.fromkeys('0123456789'))
    for file_name in file_list:
        print("old name :" + file_name)
        print("new name :" +file_name.translate(table))
        os.rename(file_name, file_name.translate(table))

    os.chdir(current_path)
rename()
