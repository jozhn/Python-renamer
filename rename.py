import os

def renamer(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        thisDir = os.path.join('%s%s' % (filepath, allDir))
        if os.path.isdir(thisDir)==True:
            #print(allDir+' '+thisDir)
            for file in os.listdir(thisDir):
                if os.path.isfile(os.path.join(thisDir,file))==True:
                    newname=allDir+'-'+file
                    os.rename(os.path.join(thisDir,file) , os.path.join(thisDir,newname))
                    #print('ok')

if __name__ == '__main__':
    filePath = "E:\\工程\\test\\"
    renamer(filePath)
    print('Complete!')

