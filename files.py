import os
import glob
import time

#------------------ get current working directory

print(os.getcwd())

#------------------ change working directory

os.chdir('d:/')

print(os.getcwd())

#------------------ get directory name and file name

file = "d:/test.txt"

print(os.path.dirname(file))
print(os.path.basename(file))

#------------------ append path

dirPath = os.path.join(os.getcwd(), 'python_projects')

print(dirPath)

#------------------ split full file path into array

paths = dirPath.split('\\')        # \ is escape sequence

print(paths)

#------------------ get file name and extension

fileName = '2015_syllabus_11_mathematics_new.pdf'

(shortName, extension) = os.path.splitext(fileName)

print(shortName)

print(extension)

#------------------ get file information

metaData = os.stat('d:/2015_syllabus_11_mathematics_new.pdf')

print('Size ', metaData.st_size, 'bytes')


def pad(x):
    if x < 10:
        return '0' + str(x)
    else:
        return x

createdTime = time.localtime(metaData.st_mtime)
print('Created time ')
print(str(createdTime.tm_hour) + ':' + str(pad(createdTime.tm_min)) + ' on ' + str(createdTime.tm_mon) + '/' + str(createdTime.tm_mday) + '/' + str(createdTime.tm_year))

#------------------ walk through the directories
for dirpath, dirs, files in os.walk("d:/vm"):
	print(dirpath)