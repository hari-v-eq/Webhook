
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests


def home(request):
    return HttpResponse('Hello World!')



@csrf_exempt
def webhook(request):
    # data={"key":"values"}
    r = requests.get('https://009f-49-36-90-131.in.ngrok.io/Webhook_Create_Subscription/')
    r.json()
   
    return JsonResponse(r,safe=False)
    # return JsonResponse({'foo':'bar'})