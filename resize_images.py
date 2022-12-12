import cv2
import os
import torch
import torch.nn.functional as F
import numpy as np

source = "C:\\Users\\Tom\\CIS5650\\KAIR_4_Channel\\testsets\\cornell_og_L_low"

for root, dirs, files in os.walk(source):
    for file in files:
        if file.endswith(".png"):
            filename = os.path.join(root, file)
            image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
            print(image)
            scaled = cv2.resize(image, (400, 400), interpolation = cv2.INTER_AREA)
            cv2.imwrite(filename ,scaled)
            print(image)
            print("Resize" + filename)
        if file.endswith(".pt"):
            filename = os.path.join(root, file)
            g_buffer = torch.load(filename)
            g_buffer = cv2.resize(g_buffer, (400, 400), interpolation = cv2.INTER_AREA)
            torch.save(g_buffer, filename)




