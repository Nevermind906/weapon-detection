import numpy as np
import cv2
import os

labelsPath = os.path.join("data", "yolo.names")
LABELS = open(labelsPath).read().strip().split("\n")

weightsPath = os.path.join("data", "yolov3.weights")
configPath = os.path.join("data", "yolov3_custom_train.cfg")

net = cv2.dnn.readNetFromDarknet(configPath,weightsPath)
