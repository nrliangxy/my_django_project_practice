from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
import os
from cmdb import models


def orm(request):
    # 增加创建方法1
    # models.UserInfo.objects.create(
    #     username='nrliangxy',
    #     password='123'
    # )
    # 增加创建方法2
    # obj = models.UserInfo(username='xiaoyong', password='991')
    # obj.save()
    # 增加创建方法3
    # dic = {'username':'nr', 'password':'999'}
    # models.UserInfo.objects.create(**dic)
    # result = models.UserInfo.objects.all()
    # result = models.UserInfo.objects.filter(username='xiaoyong', password='991')
    # for row in result:
    #     print(row.id, row.username, row.password)
    # print(result)
    # return HttpResponse('ok')
    # 删除
    # models.UserInfo.objects.filter(id=4).delete()
    # models.UserGroup.objects.create(title="a little goal now")
    # models.UserGroup.objects.filter(uid=4).update(title='build a website')
    # obj = models.UserGroup.objects.filter(uid=4).first()
    # obj.title = 'crawl the data'
    # obj.save()
    # obj = models.UserInfo.objects.all().first()
    # print(obj.user_group.uid)
    models.UserInfo.objects.create(
        username='snow',
        password='125fdggg6fdfdgghhh',
        gender='male',
        email='fdgd@qq.com',
        url='http:www.fdgdg.com',
        ip='425.365',
        user_group_id='1'
    )
    return HttpResponse('ok')


class Home(View):
    def dispatch(self, request, *args, **kwargs):
        print('before')
        result = super(Home, self).dispatch(request, *args, **kwargs)
        print('after')
        return result
    
    def get(self, request):
        print(request.method)
        return render(request, 'home.html')
    
    def post(self, request):
        print(request.method)
        return render(request, 'home.html')


# def home(request):
#     return HttpResponse('<h1>Hello</h1>')

from django.core.files.uploadedfile import InMemoryUploadedFile


def login(request):
    # request 包含了用户提交的所有信息
    # 获取用户提交方法
    # print(request.method)
    # v = request.POST.get('wj')
    # print(v)
    # obj = request.FILES.get('wj')  # FILES只取上传文件
    # print(obj, type(obj), obj.name)
    # file_path = os.path.join('upload', obj.name)
    # for i in obj.chunks():
    #     with open(file_path, 'wb') as f_read:
    #         f_read.write(i)
    #     print(i)
    error_msg = ""
    # print(request.POST.getlist('city'))
    if request.method == "POST":
        # 获取用户通过post提交过来的数据
        
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        print(user, pwd)
        # obj = models.UserInfo.objects.filter(username=user, password=pwd)
        # for i in obj:
        #     print(i.username)
        obj = models.UserInfo.objects.filter(username=user, password=pwd).first()
        # count = models.UserInfo.objects.filter(username=user, password=pwd).count()
        print(obj.username)
        if obj:
            # 去跳转到
            return redirect('/cmdb/index1/')
        else:
            # 用户名密码不匹配
            error_msg = "用户名或密码错误"
            # user = request.POST['user']
            # pwd = request.POST['pwd']
            # print(user, pwd)
    return render(request, 'login.html', {'error_msg': error_msg})


USER_LIST = [
    {'username': 'process', 'email': 'fdg@fd.com', 'gender': 'male'},
]

# USER_DICT = {
#     'k1': 'root1',
#     'k2': 'root2',
#     'k3': 'root3',
#     'k4': 'root4'
# }


USER_DICT = {
    '1': {'name': 'root1', 'email1': 'root@live1.com'},
    '2': {'name': 'root2', 'email1': 'root@live2.com'},
    '3': {'name': 'root3', 'email1': 'root@live3.com'},
    '4': {'name': 'root4', 'email1': 'root@live4.com'},
    '5': {'name': 'root5', 'email1': 'root@live5.com'}
}


def index1(request):
    return render(request, 'index1.html')


def user_info(request):
    user_list = models.UserInfo.objects.all()
    # for row in user_list:
    #     print(row.id)
    #     print(row.user_group.uid)
    #     print(row.user_group.title)
    # print(user_list.query)
    group_list = models.UserGroup.objects.all()
    return render(request, 'user_info.html', {'user_list': user_list, 'group_list': group_list})


def userdetail(request, nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    # 取单条数据，如何不存在，直接报错
    # obj = models.UserInfo.objects.get(id=nid)
    return render(request, 'user_detail.html', {'obj': obj})


def index(requset, uid, nid):
    print(requset.path_info)
    from django.urls import reverse
    # from ipdb import set_trace
    # set_trace()
    # v = reverse('indexx', args=(1, 3,))
    v = reverse('indexx', kwargs={"nid": 1, "uid": 99})
    print(v)
    return render(requset, 'index.html', {'user_dict': USER_DICT})


def detail(request, nid, uid):
    # print(nid, uid)
    # return HttpResponse(nid)
    # nid = request.GET.get('nid')
    detail_info = USER_DICT[nid]
    return render(request, 'detail.html', {'detail_info': detail_info})


# for index in range(20):
#     temp = {'username': 'process' + str(index), 'email': 'fdg@fd.com', 'gender': 'male'}
#     USER_LIST.append(temp)


# def home(request):
#     # print(request.GET.get('nid'))
#     if request.method == "POST":
#         # 获取用户提交的数据
#         u = request.POST.get('username')
#         e = request.POST.get('email')
#         g = request.POST.get('gender')
#         temp = {'username': u, 'email': e, 'gender': g}
#         USER_LIST.append(temp)
#     return render(request, 'home.html', {'user_list': USER_LIST})
# def index(request):
#     return HttpResponse('index')

# def login(request):
#     # string ="""
#     # <form>
#     # <input type='text' />
#     # </form>
#     # """
#     # f = open('templates/login.html', 'r', encoding='utf-8')
#     # data = f.read()
#     # f.close()
#     # return HttpResponse(data)
#     return render(request, 'login.html')
