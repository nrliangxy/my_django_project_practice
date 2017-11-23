from django.shortcuts import render, HttpResponse, redirect
from monitor import models


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
                hostname = h,
                ip = i,
                port = p,
                b_id = b
                )
            return redirect('/host')