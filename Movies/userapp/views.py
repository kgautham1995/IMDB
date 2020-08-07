from django.shortcuts import render,redirect
from userapp.forms import Usersignup,Userlogin
from django.contrib import messages
from userapp.models import Userlogintable
from movies_app.models import Moviemodel
from django.core.paginator import Paginator

def signuppage(request):
    return render(request,"usersignup.html",{"forms":Usersignup})
def savesignup(request):
    x=request.POST.get("username")
    y=request.POST.get("pas")
    print(x)
    print(y)
    us=Usersignup(request.POST)
    if us.is_valid():
        us.save()
        Userlogintable(usrname=x, pas=y).save()
        messages.success(request,"SignUp Successfully")
        return redirect("signuppage")
    else:
        messages.error(request,"Invalid Details")
        return redirect("signuppage")
def userlogin(request):
    return render(request,"userlogin.html",{"forms":Userlogin})
def userloginhome(request):
    n = request.POST.get("usrname")
    a = request.POST.get("pas")
    try:
        Userlogintable.objects.get(usrname=n, pas=a)
        x = Moviemodel.objects.all()
        p = Paginator(x, 3)
        page_no = request.GET.get("pno")
        if page_no:
            page = p.page(page_no)
        else:
            page = p.page(1)
        return render(request, "userpage.html", {"data": page,"name":n})

    except Userlogintable.DoesNotExist:
        messages.error(request, "Invalid User")
        return redirect("userlogin")
def searchaction(request):
    x=request.POST.get("s1")
    try:
        Moviemodel.objects.get(moviename=x)
        a=Moviemodel.objects.values('moviename')
        print(a)
        return render(request,"searchpage.html",{"data":a})
    except Moviemodel.DoesNotExist:
        messages.error(request,"Not Found")
        return render(request,"searchpage.html")