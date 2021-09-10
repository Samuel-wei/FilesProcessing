# FilesProcessing
Merge multiple file into a file


# Merge txt file

[https://zhuanlan.zhihu.com/p/98124110](https://zhuanlan.zhihu.com/p/98124110)


base/

├── fileA.txt

├── fileA2.xls

├── fileA3.xls

├── fileA4.pdf

├── sub1

│   ├── fileB.txt

│   ├── fileB2.xls

│   └── fileB3.pdf

└── sub2

    ├── fileB.txt
    
    ├── fileC2.xls
    
    └── fileC3.pdf


Mergefile.py


## Traverse all file under path and subdirectory
[python获取指定目录下所有文件名os.walk和os.listdir](https://www.cnblogs.com/cloud-ken/p/10017093.html)

    os.walk()
    
    os.listdir()
    
    os.path.splitext()
    
## read and write in .txt as lines

[Python读取一个文件夹下的所有txt文件，并按行保存](https://blog.csdn.net/suyunzzz/article/details/104727729)

[python读取多层嵌套文件夹中的文件实例](https://cloud.tencent.com/developer/article/1742319)

Mergefile.py

## Read a batch of file and write into the target file

[Python 之批量读取文件](https://blog.csdn.net/kanon122500000/article/details/57111153?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link)

os.listdir(dirname)可以列出dirname下的目录和文件
