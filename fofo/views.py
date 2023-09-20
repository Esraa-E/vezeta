from django.shortcuts import render,redirect
from .models import profile,reservation,comment
from .forms import reservationform,commentform,proform
# Create your views here.
def snu(request):

    return render(request,'doctors_list.html',{'pro' : profile.objects.all()})


def details(request,id):
    details=profile.objects.get(pk=id)
    form=commentform(request.POST or None)
    if form.is_valid():
        form=form.save(commit=False)
        form.post=details
        form.save()
        return redirect('sun')
    return render(request,'doctors_detail.html',{'detail':details,'form':form})


def reserv(request,id):
    reser=profile.objects.get(pk=id)
    return render(request,'reserv.html',{'reserv':reser,})


def book(request,id):
    doct=profile.objects.get(pk=id)
    form=reservationform(request.POST or None)
    if form.is_valid():
        form=form.save(commit=False)
        form.doc=doct
        form.save()
        return redirect('sun')
    return render(request,'book.html',{'form':form})


def update(request,id):
    res=reservation.objects.get(pk=id)
    form=reservationform(instance=res)
    if request.method=='POST':
        form=reservationform(request.POST, instance=res)
        if form.is_valid():
            form.save()
            return redirect('sun')
    
    return render(request,'update.html',{'form':form})


def delete(request,id):
    dele=reservation.objects.get(pk=id)
    if request.method=='POST':
        dele.delete()
        return redirect('sun')
    return render(request,'delete.html')
     


from .forms import mysignup
from django.contrib.auth import login
def signup(request):
    form=mysignup(request.POST or None , request.FILES or None)
    if form.is_valid():
        user=form.save()
        login(request,user)
        return redirect('sun')
    return render(request,'signup.html',{'form':form})



def commentt(request,id):
    comns=profile.objects.get(pk=id)
    return render(request,'comment.html',{'comns':comns})




def proff(request):
    form=proform()
    if request.method=='POST':
        form=proform(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('sun')
    return render(request,'profile.html',{'form':form})






def searcch(request):
    if request.method=="POST":
        searched=request.POST['searched']
        profiles=profile.objects.filter(name__contains=searched)
    
    
    
    return render(request,'searchh.html',{'pro':profiles})