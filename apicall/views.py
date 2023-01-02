from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import render,HttpResponse
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
@api_view(['GET', 'POST'])
def n_sender(request):
    with open(os.path.join(BASE_DIR+"/video/Debug.zip"), 'rb') as f:
            data = f.read()     
    response = HttpResponse(data, content_type='application/vnd.mp4')
    response['Content-Disposition'] = 'attachment; filename="Debug.zip"'
    return response