import shutil
import os


source ="C:\\Users\\Tom\\CIS5650\\datagen\\training_data\\obj_test"
train_H = "C:\\Users\\Tom\\CIS5650\\KAIR_4_Channel\\trainsets\\bunnyH"
train_L = "C:\\Users\\Tom\\CIS5650\\KAIR_4_Channel\\trainsets\\bunnyL"
test_H = "C:\\Users\\Tom\\CIS5650\\KAIR_4_Channel\\testsets\\bunnyH"
test_L = "C:\\Users\\Tom\\CIS5650\\KAIR_4_Channel\\testsets\\bunnyL"
i = 0
for root, dirs, files in os.walk(source):
    if i < 32:
        dest_H = test_H
        dest_L = test_L
    else:
        dest_H = train_H
        dest_L = train_L
    for filename in files:
        if filename.endswith("spp_5000.png"):
            shutil.copy(os.path.join(root, filename), dest_H)
            print("COPIED " + filename + " TO " + dest_H)
        else:
            shutil.copy( os.path.join(root, filename), dest_L)
            print("COPIED " + filename + " TO " + dest_L)
    if files:
        i += 1