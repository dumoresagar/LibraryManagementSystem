from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def loginView(request):
    if request.method == 'POST':
        u = request.POST.get("un")
        p = request.POST.get("pw")
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect("show_book")
        else:
            messages.error(request,"Invalid username or password")
    template_name = 'Account/login.html'
    context = {}
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect("login")

