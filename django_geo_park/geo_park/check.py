from ultralytics import YOLO
from PIL import Image
print("Hello")

def ml(img):
        res = "Неизвестный камень"
        path_model = 'best.pt'
        model = YOLO(path_model)
        mode = model.predict(source=img, max_det=1)
    
        try:
            result = int(mode[0].boxes.cls[0].item())
            print(result)
            result2 = round(float(mode[0].boxes.conf[0].item()), 2)

            if result == 0:
                res = "Эдипированный базальт"
            elif result == 1:
                res = "Базальт"
            elif result == 2:
                res = "Гнейс"
            elif result == 3:
                res = "Конгломерат"
            elif result == 4:
                res = "Кварц"
            else:
                res = "Неизвестный камень"
            return ([res, result2])
        except:
            return ("Неизвестный камень")
        
img_pil = Image.open('kvarc_mineral_2.jpg')
stone = ml(img_pil)
print(stone)