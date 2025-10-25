from django.http import HttpResponse
from django.shortcuts import render
from indexapp.models import event, gallery
from aboutapp.models import member
from eventapp.models import programs, latprograms, upcprograms
from contact.models import contactenq
from galleryapp.models import gallimg, gallimg1
from serviceapp.models import  servicedetail, servicedetaill
def homepage(request):
    eventimg=event.objects.all()
    galleryimg=gallery.objects.all()
    indexdic={'eventimg':eventimg,
              'galleryimg':galleryimg}
    return render (request,'index.html',indexdic)

def aboutpage(request):
   memberdetail=member.objects.all()

   return render (request, 'about.html',{'memberdetail':memberdetail})

def eventpage(request):
    programdetail=programs.objects.all()
    
    latprogramdetail=latprograms.objects.all()

    upcprogramsdetail=upcprograms.objects.all()

    eventdic={'programdetail':programdetail,
              'latprogramdetail':latprogramdetail,
              'upcprogramsdetail':upcprogramsdetail}

    return render(request,'event.html', eventdic)

def eventdetail(request,id):
    eventdetail=programs.objects.get(id=id)
    eventdet={'eventdetail':eventdetail,}
    return render(request,"eventdetail.html", eventdet)

def lateventdetail(request,id):
    lateventdetail=latprograms.objects.get(id=id)
    leventdet={'lateventdetail':lateventdetail,}
    return render(request,"lateventdetail.html", leventdet)

def upceventdetail(request,id):
    upceventdetail=upcprograms.objects.get(id=id)
    ueventdet={'upceventdetail':upceventdetail}
    return render(request,"upceventdetail.html", ueventdet)


def servicepage(request):
    # service_title=servicetitle.objects.all()
    service_detail=servicedetail.objects.all()
    service_detaill=servicedetaill.objects.all()

    servdic={'service_detail':service_detail,
             'service_detaill':service_detaill}
    return render(request,'services.html',servdic)


def gallerypage(request):
    gall_img=gallimg.objects.all()
    gall_img1=gallimg1.objects.all()
    galldic={'gall_img':gall_img,
             'gall_img1':gall_img1}
    return render(request,'gallery.html', galldic)


def contactpage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        event_type=request.POST.get('event_type')
        event_date=request.POST.get('event_date')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        enq=contactenq(name=name, email=email,phone=phone,
                       event_type=event_type,event_date=event_date,subject=subject,
                       message=message)
        enq.save()
    return render(request,'contact.html')

    