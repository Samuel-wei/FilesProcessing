#utf-8
# Copyright from sharebee.cn Inc, all rights reserved.
# Author: Samuel
# September 6, 2021

import os

# Traverse all txt file under path
# Reference: https://cloud.tencent.com/developer/article/1742319

loop_path = "/home/workspace/DahengImage/AcquisitionImages/suhigh20210914/0915v0"
new_file = '/home/workspace/DahengImage/AcquisitionImages/suhigh20210914/0915v0/20210915config.txt'

store_readable_file = []
def check_if_dir(variable_path):
	"loop each file under path, return real file"
	temp_list = os.listdir(variable_path)
	for temp_list_each in temp_list:
		if os.path.isfile(variable_path + '/' + temp_list_each):  # Check whether it is file? if file going on. if path executing the else block.
			read_file = variable_path + '/' + temp_list_each
			if os.path.splitext(read_file)[-1] == '.txt':
				store_readable_file.append(read_file) 
				# print(read_file)
				return store_readable_file
			else:
				continue
		else:
			check_if_dir(variable_path + '/' + temp_list_each)

check_if_dir(loop_path)
# print(str(store_readable_file))

# Reference:https://blog.csdn.net/kanon122500000/article/details/57111153?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link

def each_file_write(readable_files):
	"""Loop file contents with each line and write into the target file from path list that storage as txtfile."""
	with open(new_file, 'w') as file_object:
		for readable_file in readable_files:
			file_object.write(str(readable_file) + '\n')
			filein = open(readable_file, 'r')   #Open txt file to search path of readable file
			#print(filein)
			# loop write file contents with each lines				
			for line in filein:
				file_object.write(line)
				# print(line)
			file_object.write('\n' + '\n')
		filein.close()

readable_files = store_readable_file
each_file_write(readable_files)


