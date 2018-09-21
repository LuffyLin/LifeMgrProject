from django.shortcuts import render
from sport.models import sportitem, sportrecord
from sport.serializers import SportItemSerializer,SportRecordSerializer
from rest_framework import viewsets

# =============   sport ViewSet  ===============================
# function desc. : 運動項目列表 ViewSet
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/09/21
class SportItemViewSet(viewsets.ModelViewSet):
    queryset = sportitem.objects.all()
    serializer_class = SportItemSerializer

# function desc. : 個人運動紀錄管理 ViewSet
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/09/21
class SportRecordViewSet(viewsets.ModelViewSet):
    queryset = sportrecord.objects.all()
    serializer_class = SportRecordSerializer

# =============   sport page deal  ===============================
# function desc. : 運動項目列表
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/09/21
def sportitem(request):
    title = "運動項目列表"
    return render(request, 'sport/sportitem.html', locals())

# function desc. : 個人運動紀錄管理
# parameter : id(預設:0)
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/09/21
def sportrecord(request,id = 0):
    pass

# # function desc. : 個人運動紀錄管理 - 新增
# # parameter : id
# # create user : Luffy Lin
# # modify user : Luffy Lin
# # modify date : 2018/09/21
# def sportrecord_new(request,id):
#     pass

# # function desc. : 個人運動紀錄管理 - 更新
# # parameter : id
# # create user : Luffy Lin
# # modify user : Luffy Lin
# # modify date : 2018/09/21
# def sportrecord_update(request,id):
#     pass

# # function desc. : 個人運動紀錄管理 - 刪除
# # parameter : id
# # create user : Luffy Lin
# # modify user : Luffy Lin
# # modify date : 2018/09/21
# def sportrecord_delete(request,id):
#     pass

# # function desc. : 個人運動紀錄管理 - 搜尋
# # parameter : id
# # create user : Luffy Lin
# # modify user : Luffy Lin
# # modify date : 2018/09/21
# def sportrecord_search(request,id):
#     pass