import datetime
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.encoding import smart_str

from verify.models import Verify

def todict(source):
    target = {}
    for item in source:
        target.__setitem__(item.get('name'), item.get('value'))
    return target

def get_verificationcode(request):
    if request.method == "GET":
        operator = request.COOKIES.get("operator",'')
        imglist_obj = Verify.objects.filter(status=0)[:16]
        # uptime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) #有错，但不知道为啥
        uptime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        expiretime = str((datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S'))
        for i in imglist_obj:
            Verify.objects.filter(path=i.path).update(status=1,uptime=uptime,expiretime=expiretime)
        print(uptime)
        print(expiretime)
        imglist = []
        for i in imglist_obj:
            imglist.append(i.path)
        # print(operator)
        # return render(request,'verify.html',{'imglist':imglist})
        return render(request, 'name.html', {'imglist': imglist})
    if request.method == "POST":
        result_dic = request.POST.dict()
        result_dic.pop('csrfmiddlewaretoken')
        operator = result_dic.pop('operator')
        print(result_dic)
        for key,values in result_dic.items():
            Verify.objects.filter(path=key,status=1).update(tab=values,operator=operator,status=2)
        imglist_obj = Verify.objects.filter(status=0)[:16]
        uptime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        expiretime = str((datetime.datetime.now() + datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S'))
        for i in imglist_obj:
            Verify.objects.filter(path=i.path).update(status=1, uptime=uptime, expiretime=expiretime)
        print(uptime)
        print(expiretime)
        imglist = []
        for i in imglist_obj:
            imglist.append(i.path)
        # response = HttpResponseRedirect(reverse('home'))
        # response = render(request, 'vc.html', {'imglist': imglist})
        # print(type(operator))
        # response.set_cookie("operator",smart_str(operator))
        return render(request, 'vc.html', {'imglist': imglist})

def get_count(request):
    if request.method == "POST":
        operator = request.POST.get("operator",'')
        records = Verify.objects.filter(operator=operator,status=2)
        count = records.count()
        return HttpResponse(count)
    return render(request,"404.html")

def check_verificationcode(request):
    if request.method == "GET":
        operator = request.COOKIES.get("operator",'')
        imglist_obj = Verify.objects.filter(status=0)[:16]
        # uptime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) #有错，但不知道为啥
        uptime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        expiretime = str((datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S'))
        for i in imglist_obj:
            Verify.objects.filter(path=i.path).update(status=1,uptime=uptime,expiretime=expiretime)
        # print(uptime)
        # print(expiretime)
        # imglist = []
        # for i in imglist_obj:
        #     imglist.append(i.path)
        # print(operator)
        # return render(request,'verify.html',{'imglist':imglist})
        return render(request, 'name.html', {'imglist': imglist_obj})
    # if request.method == "POST":
    #     result_dic = request.POST.dict()
    #     result_dic.pop('csrfmiddlewaretoken')
    #     operator = result_dic.pop('operator')
    #     print(result_dic)
    #     for key,values in result_dic.items():
    #         Verify.objects.filter(path=key,status=1).update(tab=values,operator=operator,status=2)
    #     imglist_obj = Verify.objects.filter(status=0)[:16]
    #     uptime = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #     expiretime = str((datetime.datetime.now() + datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S'))
    #     for i in imglist_obj:
    #         Verify.objects.filter(path=i.path).update(status=1, uptime=uptime, expiretime=expiretime)
    #     print(uptime)
    #     print(expiretime)
    #     imglist = []
    #     for i in imglist_obj:
    #         imglist.append(i.path)
    #     # response = HttpResponseRedirect(reverse('home'))
    #     # response = render(request, 'vc.html', {'imglist': imglist})
    #     # print(type(operator))
    #     # response.set_cookie("operator",smart_str(operator))
    #     return render(request, 'vc.html', {'imglist': imglist})