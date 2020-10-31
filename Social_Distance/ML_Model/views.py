from Profiles.serializers import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import generics, permissions, status, viewsets
from django.http import JsonResponse
from . import ml_model
import cv2
import numpy as np

@csrf_exempt
def run_social(request):

    data = {"success": False}

    if request.method == "POST":
        if request.FILES.get("image", None) is not None:
            image = _grab_image(stream=request.FILES["image"])
            data['success'] = ml_model.test(image)

    # return a JSON response
    return JsonResponse(data)

def _grab_image(stream=None):
    data = stream.read()

    image = np.asarray(bytearray(data), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    return image