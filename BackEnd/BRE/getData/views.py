from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse

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
    #est = getPredictions(request.POST['locations'],request.POST['sqft'],request.POST['bath'],request.POST['bhk'])
    print(request)
    data = {"body" :{"Hello":123456} }
    return JsonResponse({"Hello":"HI"})
    #return redirect(request.META['HTTP_REFERER'])