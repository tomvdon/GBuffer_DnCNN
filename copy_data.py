import shutil
import os

source ="C:\\Users\\Tom\\CIS5650\\KAIR\\my_data\\cornell"
dest_H = "C:\\Users\\Tom\\CIS5650\\KAIR\\my_data\\H"
dest_L = "C:\\Users\\Tom\\CIS5650\\KAIR\\my_data\\L"
iter = -1
newfilenum = 0
for root, dirs, files in os.walk(source):
    for filename in files:
        print(filename)
        if filename.endswith("spp_5000.png"):
            for i in range(16):
                newname = str(i + 16 * iter) + ".png"
                shutil.copy(os.path.join(root, filename), dest_H + "\\"+ newname)
                print("COPIED " + filename + " TO " + dest_H + "\\"+ newname)
        else:
            newname = str(newfilenum) + ".png"
            shutil.copy( os.path.join(root, filename), dest_L + "\\" + newname)
            print("COPIED " + filename + " TO " + dest_L + "\\"+ newname)
            newfilenum += 1
    iter+=1