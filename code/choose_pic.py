import os
import shutil
import random
def choose_au(pic_folder, des_folder, size):
    count = 0
    for filepath, dirnames, filenames in os.walk(pic_folder):
        for filename in filenames:
            p = random.random()
            if p > 0.1:
                old_path = filepath + '/' + filename
                shutil.move(old_path, des_folder)
                count += 1
            if count == size:
                return

def choose_tp(pic_folder, des_folder, size):
    count = 0
    for filepath, dirnames, filenames in os.walk(pic_folder):
        for filename in filenames:
            p = random.random()
            if p > 0.01:
                old_path = filepath + '/' + filename
                shutil.move(old_path, des_folder)
                count += 1
            if count == size:
                return

# choose_au('/Users/yupeijia/Downloads/CASIA2/Au', '/Users/yupeijia/Downloads/CASIA2000/Au', size)
# choose_tp('/Users/yupeijia/Downloads/CASIA2/Tp', '/Users/yupeijia/Downloads/CASIA2000/Tp', size)
