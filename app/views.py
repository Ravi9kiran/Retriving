from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def Ravi(request):
    qst=Topic.objects.all()
    d={'Topic':qst}
    return render(request,'Ravi.html',d)

def Kiran(request):
    qst=Webpages.objects.all()
    qst=Webpages.objects.filter(name__startswith='d')
    qst=Webpages.objects.filter(Topic_name='cricket')
    qst=Webpages.objects.exclude(Topic_name='cricket')
    qst=Webpages.objects.all()[:6:]
    qst=Webpages.objects.all().order_by('-name')
    qst=Webpages.objects.filter(Topic_name='kabaddi').order_by('-name')
    qst=Webpages.objects.all().order_by(Length('name'))
    qst=Webpages.objects.all().order_by(Length('name').desc())
    qst=Webpages.objects.filter(Url__startswith='https')
    qst=Webpages.objects.filter(Url__endswith='com')
    qst=Webpages.objects.filter(name__contains='s')
    qst=Webpages.objects.filter(Q(Topic_name='cricket') | Q(name='Dhawan'))
    qst=Webpages.objects.filter(Q(Topic_name='Batminton') & Q(Url__startswith='https'))
    qst=Webpages.objects.all()
    d={'webpage':qst}
    return render(request,'Kiran.html',d)

def Varikuti(request):
    qst=AccessRecords.objects.all()
    qst=AccessRecords.objects.all().order_by('date')
    qst=AccessRecords.objects.filter(date='2001-06-07')    
    qst=AccessRecords.objects.filter(date__gt='2001-06-07')    
    qst=AccessRecords.objects.filter(date__gte='2001-06-07') 
    qst=AccessRecords.objects.filter(date__lte='2023-01-14')
    qst=AccessRecords.objects.filter(date__year='2023')  
    qst=AccessRecords.objects.filter(date__month='1')    
    qst=AccessRecords.objects.filter(date__day='14')   
    qst=AccessRecords.objects.filter(date__year__gt='2022')
    d={'AccessRecords':qst}
    return render(request,'Varikuti.html',d)