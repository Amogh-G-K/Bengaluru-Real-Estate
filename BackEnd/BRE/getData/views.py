from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import json

from getData.util import *
#import util
# Create your views here.
def index(request):
    #template = loader.get_template('../../../FrontEnd/index.html')
    #return render(request,'C:/Users/admin/Desktop/mani workspace/Bengaluru Real Estate/FrontEnd/index.html')
    #print(getLocations())
    return render(request,'base.html',{"locations":getLocationNames()})

def estimation(request):
    print("called")
    print(request.POST)
    print(json.loads(request.body))
    req = json.loads(request.body)
    print(req['locations'])
    print(req['sqft'])
    print(req['bath'])
    print(req['bhk'])
    est = getPredictions(req['locations'],req['sqft'],req['bath'],req['bhk'])
    print(est);
    return JsonResponse({"FinalEstimation":est})