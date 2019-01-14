import urllib.request

def read_file():
    file_check = open(r"C:\Users\Ajeet\Desktop\python_mini_projects\test.txt")
    contents = file_check.read()
    print(contents)
    file_check.close()
    check(contents)
def check(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    #urllib is a module used to read data from the internet and urlopen is a function present in urllib module
    #http://www.wdylike.appspot.com/?q=shot is a site developed by google to check profanity
    response = connection.read()
    #print(response)
    connection.close()
    if "true" in response:
        print("Profanity Found!!!")
    elif "false" in response:
        print("This document is free from profanity")
    else:
        print("could not read the document properly!!!!")
read_file()
