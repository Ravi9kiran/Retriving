from django.shortcuts import render
from app.models import *

# Create your views here.
def Ravi(request):
    qst=Topic.objects.all()
    d={'Topic':qst}
    return render(request,'Ravi.html',d)

def Kiran(request):
    qst=Webpages.objects.all()
    d={'webpage':qst}
    return render(request,'Kiran.html',d)

def Varikuti(request):
    qst=AccessRecords.objects.all()
    d={'AccessRecords':qst}
    return render(request,'Varikuti.html',d)