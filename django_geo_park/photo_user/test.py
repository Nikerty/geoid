import numpy as np
from PIL import Image
from ultralytics import YOLO

path_img = "name.png"
path_model = '{}/best.pt'.format(".")
model = YOLO(path_model)
im1 = Image.open(path_img)
result = model.predict(source=im1, max_det=1)[0].boxes.conf[0].item()#.cls[0].item())

# if result == 0:
#     result = "Эдипированный базальт"
# elif result == 1:
#     result = "Базальт"
# elif result == 2:
#     result = "Гнейс"
# elif result == 3:
#     result = "Конгломерат"
# elif result == 4:
#     result = "Кварц"

print(result)