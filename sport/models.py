from django.db import models
from limit.models import user

#運動項目
class sportitem(models.Model):
    name    = models.CharField(max_length=50, blank=True, null=True, verbose_name ='運動項目')   #運動項目名稱
    cal     = models.IntegerField(verbose_name ='卡洛里(每小時/每公斤)')                           #運動消耗卡洛里calorie
    state   = models.BooleanField()                                                             #狀態(1:啟用/0:停用)
    
    cuser   = models.ForeignKey(user,models.DO_NOTHING, verbose_name ='')                       #建立人員
    cdate   = models.DateTimeField(auto_now_add=True, verbose_name ='')                         #建立日期
    mdate   = models.DateTimeField(auto_now=True, verbose_name ='')                             #修改日期
    class Meta:
        db_table = 'sport_sportitem'

#運動管理
class sportrecord(models.Model):
    sportid = models.ForeignKey(sportitem,models.DO_NOTHING, verbose_name ='運動項目')           #運動項目
    weight  = models.DecimalField (max_digits=4, decimal_places=1, verbose_name ='體重')        #體重(公斤)
    cal     = models.IntegerField(verbose_name ='運動消耗卡洛里calorie')                          #運動消耗卡洛里calorie
    duration = models.IntegerField(verbose_name ='運動持續時間(分鐘)')                            #運動持續時間(分鐘)
    
    cuser   = models.ForeignKey(user,models.DO_NOTHING)                                         #建立人員
    cdate   = models.DateTimeField(auto_now_add=True)                       #建立日期
    mdate   = models.DateTimeField(auto_now=True)                           #修改日期
    class Meta:
        db_table = 'sport_sportrecord'

#體重管理
class weightrecord(models.Model):
    weight  = models.DecimalField (max_digits=4, decimal_places=1, verbose_name ='體重(公斤)')      #體重(公斤)
    
    cuser   = models.ForeignKey(user,models.DO_NOTHING, verbose_name ='')                       #建立人員
    cdate   = models.DateTimeField(auto_now_add=True, verbose_name ='')                         #建立日期
    mdate   = models.DateTimeField(auto_now=True, verbose_name ='')                             #修改日期
    class Meta:
        db_table = 'sport_weightrecord'