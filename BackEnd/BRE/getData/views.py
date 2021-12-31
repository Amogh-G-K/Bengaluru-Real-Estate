from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

from getData.util import *
#import util
# Create your views here.
def index(request):
    #template = loader.get_template('../../../FrontEnd/index.html')
    #return render(request,'C:/Users/admin/Desktop/mani workspace/Bengaluru Real Estate/FrontEnd/index.html')
    #print(getLocations())
    return render(request,'base.html',{"locations":getLocationNames()})

def estimation(request):
    est = getPredictions(request.POST['locations'],request.POST['sqft'],request.POST['bath'],request.POST['bhk'])
    print(est)
    return redirect(request.META['HTTP_REFERER'])
    #return HttpResponse('<h1>'+str(est)+'</h1>')