import os

TARGETPATH = "D:\\test"
records = []
for currentDir, _, includedFiles in os.walk(TARGETPATH):
    if not currentDir.endswith('_BAD'): continue
    else:
        records.append(currentDir)  # 将以“_BAD”结尾的文件夹名加入records
        records.extend(includedFiles)  # 将该文件夹内的文件名列表扩展到records

# 将records写入.txt
txtFile = open(os.path.join(TARGETPATH, '02_04_BAD.txt'), 'w')
txtFile.write(os.linesep.join(records))
txtFile.close()

# 将排序后的records写入.txt
with open(os.path.join(TARGETPATH, '02_04_BAD_SORTED.txt'), 'w') as txtFile:
    txtFile.write('\n'.join(sorted(records)))