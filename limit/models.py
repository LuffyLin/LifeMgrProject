from django.db import models

# Create your models here.

#角色
class role(models.Model):
    role    = models.CharField(max_length=20, blank=True, primary_key= True)                            #角色名稱
    desc    = models.CharField(max_length=500, blank=True, null=True)                                   #角色描述
    state   = models.BooleanField()                                                                     #狀態(1:啟用,0:停用)
    class Meta:
        db_table = 'limit_role'      

#功能選單
class menu(models.Model):
    name    = models.CharField(max_length=20, blank=True)                                               #名稱
    level   = models.IntegerField()                                                                     #階層
    parent  = models.ForeignKey('self',models.DO_NOTHING,db_column ='menu_id')                          #父節點
    index   = models.IntegerField()                                                                     #排序
    state   = models.BooleanField()                                                                     #狀態(1:啟用,0:停用)
    class Meta:
        db_table = 'limit_menu'

#角色功能權限
class rolemenu(models.Model):
    menuid  = models.ForeignKey(menu,models.DO_NOTHING,db_column ='menu_id')                            #功能
    roleid  = models.ForeignKey(role,models.DO_NOTHING,db_column ='role_id')                            #階層
    index   = models.IntegerField()                                                                     #排序
    state   = models.BooleanField()                                                                     #狀態(1:啟用,0:停用)
    class Meta:
        db_table = 'limit_rolemenu'

#使用者資料表
class user(models.Model):
    email   = models.CharField(max_length=200,unique=True)                                              #email
    name    = models.CharField(max_length=50)                                                           #使用者名稱
    birthday= models.DateField()                                                                        #生日
    gender  = models.CharField(max_length=2)                                                            #性別
    password= models.CharField(max_length=20)                                                           #密碼
    class Meta:
        db_table = 'limit_user'

#使用者角色資料表
class userrole(models.Model):
    userid = models.ForeignKey(user,models.DO_NOTHING,db_column ='user_id')                             #userid   
    roleid = models.ForeignKey(role,models.DO_NOTHING,db_column ='role_id')                             #roleid
    class Meta:
        db_table = 'limit_userrole'