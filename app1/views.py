from django.shortcuts import render

# Create your views here.


def msd(request):
    return render(request,'msd.html')

def raina(request):
    return render(request,'raina.html')

def rayudu(request):
    return render(request,'rayudu.html')