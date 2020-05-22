
import hashlib
import sys, os

# 获取文件 MD5 
def get_md5(file_path):
    f = open(file_path,'rb')  
    md5_obj = hashlib.md5()
    while True:
        d = f.read(8096)
        if not d:
            break
        md5_obj.update(d)
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
    return md5

# 重命名为 MD5
def rename (dirPath:str):
    listFile = os.listdir(dirPath)

    listMd5 = {}

    for f in listFile :
        filePath = dirPath + "\\" + f
        if os.path.isdir(filePath):
            rename(filePath)
            continue
        res = get_md5(dirPath + "\\" + f)
        try:
            if listMd5[res] == 1:
                os.unlink(filePath)
        except :
            listMd5[res] = 1
            os.rename(filePath, dirPath + "\\" + res)
    return

# 重命名为 MD5 并附带扩展名
def renameWithExt (dirPath:str):
    listFile = os.listdir(dirPath)

    listMd5 = {}

    for f in listFile :
        filePath = dirPath + "\\" + f
        ext = os.path.splitext(f)
        if os.path.isdir(filePath):
            rename(filePath)
            continue
        res = get_md5(dirPath + "\\" + f)
        try:
            if listMd5[res] == 1:
                os.unlink(filePath)
        except :
            listMd5[res] = 1
            if len(ext) > 1:
                os.rename(filePath, dirPath + "\\" + res + ext[-1])
            else:
                os.rename(filePath, dirPath + "\\" + res)
    return

# 主函数
if __name__ == "__main__":
    if len(sys.argv) < 2 :
        print("Need dir path")
        exit(0)

    print("%s" % sys.argv[1])
    if not os.path.isdir(sys.argv[1]) :
        print("Invalid dir path")
        exit(0)
    renameWithExt(sys.argv[1])

    pass