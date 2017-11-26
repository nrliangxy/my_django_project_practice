from django.shortcuts import render, HttpResponse, redirect
from monitor import models
import json


# Create your views here.
def orm(request):
    # models.Buseiness.objects.create(
    #     caption="测试"
    # )
    models.Buseiness.objects.filter(id=2).update(english_name="front end")
    models.Buseiness.objects.filter(id=3).update(english_name="back end")
    models.Buseiness.objects.filter(id=4).update(english_name="test")
    return HttpResponse('ok')


def business(request):
    obj = models.Buseiness.objects.values()
    obj1 = models.Buseiness.objects.all()
    obj2 = models.Buseiness.objects.values_list()
    # for i in obj:
    #     print(i)
    #     print(type(i))
    # return HttpResponse('ok')
    return render(request, "business.html", {'v': obj, 'v1': obj1, 'v2': obj2})


def host(request):
    if request.method == "GET":
        v1 = models.Host.objects.all()  # models.Host.objects.filter(nid__gt=0)
        # for i in v1:
        #     print(i.ip)
        # return HttpResponse('ok')
        # v2 = models.Host.objects.filter(nid__gt=0).values('b__caption')
        # for row in v2:
        #     print(row['b__caption'])
        # return HttpResponse('ok')
        op_list = models.Buseiness.objects.all()
        
        # print(h,i,p,b)
        return render(request, "host.html", {'v1': v1, 'op_list': op_list})
    elif request.method == "POST":
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        models.Host.objects.create(
            hostname=h,
            ip=i,
            port=p,
            b_id=b
        )
        return redirect('/host')


def test_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        if h and len(h) < 5:
            models.Host.objects.create(
                hostname=h,
                ip=i,
                port=p,
                b_id=b
            )
            # return HttpResponse('ok')
        else:
            ret['status'] = False
            ret['error'] = '太长了'
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'
    # print(request.method, request.POST, sep='\t')
    # print(request.method, request.GET.get('user'), request.GET.get('pwd'), sep='\t')
    # import time
    # time.sleep(5)
    return HttpResponse(json.dumps(ret))


def app(request):
    if request.method == 'GET':
        app_list = models.Application.objects.all()
        host_list = models.Host.objects.all()
        return render(request, 'app.html', {"app_list": app_list, 'host_list': host_list})
    elif request.method == 'POST':
        app_name = request.POST.get('app_name')
        host_list = request.POST.getlist('host_list')
        print(app_name, host_list)
        obj = models.Application.objects.create(name=app_name)
        obj.r.add(*host_list)
        return redirect('/app')
        # for row in app_list:
        #     print(row.name, row.r.all())
        # return render(request, 'app.html', {"app_list": host_list})


def ajax_add_app(request):
    ret = {'status': True, 'error': None, 'data': None}
    app_name = request.POST.get('app_name')
    host_list = request.POST.getlist('host_list')
    obj = models.Application.objects.create(name=app_name)
    obj.r.add(*host_list)
    return HttpResponse(json.dumps(ret))
    # print(request.POST.get('app_name'))
    # print(request.POST.getlist('host_list'))
    # return HttpResponse(json.dumps(ret))
