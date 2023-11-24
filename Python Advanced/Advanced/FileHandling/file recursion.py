

from os import listdir,path
def takeFilesFromFolderRecursive(pathh,dictt):
    for el in listdir(pathh):
        current_dir_path=path.join(pathh,el)
        if  path.isdir(current_dir_path):
            dirrr=listdir(current_dir_path)
            takeFilesFromFolderRecursive(current_dir_path,dictt)
        else:
            extension=el.split('.')[-1]
            if extension not in dictt:
                dictt[extension]=[]
            dictt[extension].append(el)
    return dictt
dictt={}
dict=takeFilesFromFolderRecursive('.',dictt)
print(dictt)
