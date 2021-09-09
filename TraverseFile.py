import os 

#os.listdir(), return list of file and folder under path, but don't traverse subdirectory
def file_name_listdir(file_dir):
    for files in os.listdir(file_dir):
        print("files", files)

#file_name_listdir("/home/workspace/DeepLearning/PythonProgramming/data/battery/")

#os.walk(), return under path of files and all files of subdirectory.
def file_name_walk(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print("root", root)
        print("dirs", dirs)
        print("files", files)

# file_name_walk("/home/workspace/DeepLearning/PythonProgramming/data/battery/")

#Use global variable to saved the file names if you went to savings the file name for each call from global list.
Files_Global = []

def file_name_listdir_global(file_dir):
    for files in os.listdir(file_dir):
        Files_Global.append(files)

# file_name_listdir_global("/home/workspace/DeepLearning/PythonProgramming/data/battery/")
# file_name_listdir_global("/home/workspace/DeepLearning/PythonProgramming/data")
# print("Files_Gloabl: ", Files_Global) 

All_Files_Global = []
def all_file_name_global(file_dir):
    for files in os.walk(file_dir):
        All_Files_Global.append(files)

# all_file_name_global("/home/workspace/DeepLearning/PythonProgramming/data/battery/")
#all_file_name_global("/home/workspace/DeepLearning/PythonProgramming/data")
# print("All_Files_Gloabl: ", All_Files_Global) 
      

#local variable and function return
def file_name_listdir_local(file_dir):
    files_local = []
    for files in os.listdir(file_dir):
        files_local.append(files)
    return files_local

# file_local_1 = file_name_listdir_local("/home/workspace/DeepLearning/PythonProgramming/data")
# file_local_2 = file_name_listdir_local("/home/workspace/DeepLearning/PythonProgramming/data/battery")
# print("file_local_1: ", file_local_1)
# print("file_local_2: ", file_local_2)

#os.path.splitext function specific the file style
def file_name(file_dir):
    File_Name = []
    for files in os.listdir(file_dir):
        if os.path.splitext(files)[1] == '.txt':
            File_Name.append(files)
    return File_Name
    
# txt_file_name=file_name("/home/workspace/DeepLearning/PythonProgramming/data/")
# print("txt_file_name", txt_file_name)

# Reference: https://cloud.tencent.com/developer/article/1742319
import os
path = '/home/workspace/DeepLearning/PythonProgramming/data/battery'
path_read = []  #path_read saves all executable files

def check_if_dir(file_path):
  temp_list = os.listdir(file_path)  #put file name from file_path in temp_list
  for temp_list_each in temp_list:
    if os.path.isfile(file_path + '/' + temp_list_each):
      temp_path = file_path + '/' + temp_list_each
      if os.path.splitext(temp_path)[-1] == '.txt':  #自己需要处理的是.txt文件所以在此加一个判断
        path_read.append(temp_path)
      else:
        continue
    else:
      check_if_dir(file_path + '/' + temp_list_each)  #loop traversal

check_if_dir(path)
print(path_read)