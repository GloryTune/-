import shutil,os

count = 0
def moveFiles(path,disdir):
    global count
    dirlist = os.listdir(path)
    for i in dirlist:
        child = os.path.join('%s/%s' % (path,i))
        print(child)
        if os.path.isfile(child):
            count += 1
            shutil.move(child,os.path.join(new_path,'{}'.format(count) + '.jpg'))
            continue
        moveFiles(child,disdir)
if __name__ == '__main__':
    ori_path = 'D:/chromed/图/京东T恤图集'#原始文件夹 就是一个大文件夹下有几千个商品类的那个路径
    #path_list = os.listdir(ori_path)
    new_path = 'D:/yangtian' #要将图片都转移到新文件夹下的新文件夹路径，要提前建好
    moveFiles(ori_path,new_path)
#print(path_list)