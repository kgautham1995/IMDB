from django.shortcuts import render,redirect
from movies_app.models import Moviemodel
import json
from Movies.settings import ONLINE_MOVIES_FILE

def addmovie(request):
    dict_data = json.loads(open(ONLINE_MOVIES_FILE).read())
    movies = [x for x in dict_data['d']]
    return render(request,"addmovie.html",{"data": movies})
def savemovie(request):
    data=request.GET.get("mdata")
    a = data.split(',')
    print(a)
    x=a[0]
    print(x)
    y=a[1]
    print(y)
    z=a[2]
    print(z)
    b=a[3]
    print(b)
    c=a[5]
    print(c)
    Moviemodel(moviename=x,t_ype=y,rank=z,casting=b,release=c).save()
    return redirect("addmovie")