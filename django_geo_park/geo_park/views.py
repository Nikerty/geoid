# from ..ML_model.ml_model import ml
import ast
import base64
import json
import os
import re
import urllib
from io import BytesIO


import cv2
from django.core.files import File
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from drf_extra_fields.fields import Base64ImageField
from keras.models import load_model
from PIL import Image
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from ultralytics import YOLO
from django.shortcuts               import render

from .serializers import *


def decode_base64(data, altchars=b'+/'):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'='* (4 - missing_padding)
    return base64.b64decode(data, altchars)

def analize(request):

    try:
        #data1 = request.POST["img_user_base64"]
        
        #img_pil = Image.open(BytesIO(base64.b64decode(data1)))
        img_pil = Image.open('/home/npi/geo_park/django_geo_park/geo_park/kvarc_mineral_2.jpg')
        stone = ml(img_pil)
        data = {
            "name_photo_user": "name",
            "stone": stone,
            "percentage": f"{stone[1]*100}%",
            "Hello":"Hello"
        }
        return JsonResponse(data)
    except Exception as e:
        data = {
            "name_photo_user": "name",
            "img_user_base64": e,
            "stone": "Не найден камень",
            "percentage": "0%"

        }
        return JsonResponse(e)



        # image = Image.frombytes(BytesIO(img))
        
    
def ml(img):
        res = "Неизвестный камень"
        path_model = 'geo_park/best.pt'
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
            return [res, result2]
        except:
            return ("Неизвестный камень")
          
    
