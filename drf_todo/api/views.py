from django.http import JsonResponse
from django.shortcuts import render

def apiOverview(request):
    return  JsonResponse("aPI BASE POINT", safe=False)