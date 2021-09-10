#utf-8
# Copyright from sharebee.cn Inc, all rights reserved.
# Author: Samuel
# September 6, 2021
# Reference: https://www.cnblogs.com/cloud-ken/p/10017093.html
# https://cloud.tencent.com/developer/article/1742319

import os

# Traverse all txt file under path
# Reference: https://cloud.tencent.com/developer/article/1742319
# Reference:https://blog.csdn.net/kanon122500000/article/details/57111153?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link

loop_path = "/home/workspace/BatteryDetect/data/battery"

def check_if_dir(variable_path):
	"loop each file under path, return real file"
	temp_list = os.listdir(variable_path)
	for temp_list_each in temp_list:
		if os.path.isfile(variable_path + '/' + temp_list_each):
			read_file = variable_path + '/' + temp_list_each
			print(read_file)			
			if os.path.splitext(read_file)[-1] == '.txt':
				with open('/home/workspace/BatteryDetect/data/allbatteryconfig.txt', 'a') as file_object:
					file_object.write(str(read_file) + '\n')
					filein = open(read_file, 'r')
					#print(filein)				
					for line in filein:
						file_object.write(line)
						print(line)
					file_object.write('\n' + '\n')
					filein.close()
			else:
				continue
		else:
			check_if_dir(variable_path + '/' + temp_list_each)

check_if_dir(loop_path)