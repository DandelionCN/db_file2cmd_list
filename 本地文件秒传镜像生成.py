#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os

# os.system("c:\\sam.bat")


import subprocess
#os.system("D: && cd D:\\11111118 && echo 114>1.txt && echo 214>>1.txt ")
#nowpath = "cd D:\\1104"
#os.system("D: && "+nowpath+" && pall.bat && fall.bat")

# !/usr/bin/env python 2

# coding : utf-8 3
import hashlib
from hashlib import md5
import time
import os

front_leng = 11
input_path = "D:\\tst0002"
output_path = "D:\\tst0002\\Mirror"

def calMD5(str):
    m = md5()
    m.update(str)

    return m.hexdigest()


def calMD5ForFile(file):
    statinfo = os.stat(file)

    if int(statinfo.st_size) / (1024 * 1024) >= 1000:
        print
        "File size > 1000, move to big file..."
        return calMD5ForBigFile(file)

    m = md5()
    f = open(file, 'rb')
    m.update(f.read())
    f.close()

    return m.hexdigest()


def calMD5ForFolder(dir, MD5File):
    outfile = open(MD5File, 'w')
    for root, subdirs, files in os.walk(dir):
        for file in files:
            filefullpath = os.path.join(root, file)
            """print filefullpath"""

            filerelpath = os.path.relpath(filefullpath, dir)
            md5 = calMD5ForFile(filefullpath)
            outfile.write(filerelpath + ' ' + md5 + "\n")
    outfile.close()


def calMD5ForBigFile(file):
    m = md5()
    f = open(file, 'rb')
    buffer = 8192  # why is 8192 | 8192 is fast than 2048

    while 1:
        chunk = f.read(buffer)
        if not chunk: break
        m.update(chunk)

    f.close()
    return m.hexdigest()



def dirlist1(path, allfile):
    with open(output_path + "\\ru.bat", "a", encoding='utf-8') as fa:
        with open(output_path + "\\path.bat", "a", encoding='utf-8') as fb:
            with open(output_path + "\\file.bat", "a", encoding='utf-8') as fc:
                filelist = os.listdir(path)
                for filename in filelist: #广义
                    filepath = os.path.join(path, filename)
                    if os.path.isdir(filepath):
                        fb.write("md "+'"'+ filepath[front_leng:] +'"'+"\n") #输入
                        dirlist1(filepath, allfile)
                    # elif filepath.endswith('db'):
                        # if 'Cache' in filepath:




                return allfile


def dirlist2(path, allfile):
    with open(output_path + "\\ru.bat", "a", encoding='utf-8') as fa:
        with open(output_path + "\\path.bat", "a", encoding='utf-8') as fb:
            with open(output_path + "\\file.bat", "a", encoding='utf-8') as fc:
                filelist = os.listdir(path)

                for filename in filelist:  # 广义
                    filepath = os.path.join(path, filename)
                    if os.path.isdir(filepath):
                        dirlist2(filepath, allfile)
                    # elif filepath.endswith('db'):
                    # if 'Cache' in filepath:
                    elif os.path.getsize(filepath) > 1000000:
                        allfile.append(filepath)

                        file_md5 = calMD5ForBigFile(filepath)
                        size = os.path.getsize(filepath)
                        print('BaiduPCS-Go ru -length=' + str(size) + ' -md5=' + str(file_md5) + ' "' + str(
                            filepath[front_leng:].replace("\\", "/")) + '"')
                        fa.write('BaiduPCS-Go ru -length=' + str(size) + ' -md5=' + str(file_md5) + ' "' + str(
                            filepath[front_leng:].replace("\\", "/")) + '"' + '\n')
                        fb.write('echo BaiduPCS-Go ru -length=' + str(size) + ' -md5=' + str(file_md5) + ' "' + str(
                            filepath[front_leng:].replace("\\", "/")) + '"' + '>>' + '"' +
                                 filepath[front_leng:] + ".bat" + '"' + '\n')

                return allfile


filelist = dirlist1(input_path, [])  #[]即是空数组
filelist2 = dirlist2(input_path, [])  #[]即是空数组
# filelist = ["H:\\3441752476_南国豪苑\\000000天文\\distroastro-2.0天文操作系统Linux.iso","D:\\本地\\H第一批.txt"]
with open(output_path+"\\call.bat", "a") as fcallp:
    fcallp.write('chcp 65001\n'+output_path+'\\path.bat')
    fcallp.close()

os.system("D: && cd " + output_path +" && "+output_path+"\\call.bat")


# if __name__ == "__main__":
#     # print calMD5("Hello World!")
#
#     # t = time.time()
#     # print(calMD5ForFile("H:\\3441752476_南国豪苑\\000000天文\\distroastro-2.0天文操作系统Linux.iso"))
#     # print(time.time() - t)
#     t = time.time()
#     print(calMD5ForBigFile("H:\\3441752476_南国豪苑\\000000天文\\distroastro-2.0天文操作系统Linux.iso"))
#     print(time.time() - t, "\n")


    # t = time.time()
    # print(calMD5ForFile("E:\\OS\\ubuntu-12.04-desktop-amd64.iso"))
    # print(time.time() - t)
    # t = time.time()
    # print(calMD5ForBigFile("E:\\OS\\ubuntu-12.04-desktop-amd64.iso"))
    # print(time.time() - t, "\n")
    #
    # t = time.time()
    # print(calMD5ForFile("D:\\Virtual Machines\\Ubuntu 64-bit\\Ubuntu 64-bit-s001.vmdk"))
    # print(time.time() - t)
    # t = time.time()
    # print(calMD5ForBigFile("D:\\Virtual Machines\\Ubuntu 64-bit\\Ubuntu 64-bit-s001.vmdk"))
    # print(time.time() - t, "\n")



"""要达到预期的效果，如果仍使用os.system，有两种方法。
第一种方法是确保工作目录的变更和svn都在子进程中进行，
可以使用复合语句（如os.system('cd path-to-repo && svn ci')）
或多个语句（如os.system('cd path-to-repo; svn ci')）。
第二种方法则是先在父进程中切换工作目录(os.chdir('path-to-repo'))，
再利用1.中提到的原理，执行子进程即可(os.system('svn ci'))。"""

#cmd = 'cmd.exe c:\\sam.bat'
#os.system("D:\\1104\\pall.bat")
#os.system("D:\\1104\\fall.bat")
#p = subprocess.Popen("cmd.exe /c" + "c:\\sam.bat abc", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)



'''
curline = p.stdout.readline()
while (curline != b''):
    print(curline)
    curline = p.stdout.readline()

p.wait()
print(p.returncode)
'''
