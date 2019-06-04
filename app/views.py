from django.shortcuts import render,redirect
from .forms import *

def home(request):
    if request.method=='POST':
        form=ProfileForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ProfileForm()
        return render(request,'profile.html',{'form':form})
    return redirect('/')