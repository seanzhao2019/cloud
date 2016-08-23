#coding=utf-8
#__author__='zhao'


from datetime import datetime, date
import hashlib
import datetime
# Create your views here.

PRIORITY = 5 #1-5，level 1 need to be handled firstly
SERVICE_TYPE = 0#0==nothing
SERVICE_LIMITATION=30 #30 DAYS
TOKEN_EXPIRE=1 #1 DAY




class Check_validity(object):
    def __init__(self,timestamp,service_limitation):
        self.timestamp=timestamp
        self.service_limitation=service_limitation

    def check_token_expire(self):
        t0=datetime.datetime.now()
        diff = t0 >= (self.timestamp + datetime.timedelta(minutes=1))  # 設置爲30days後失效
        #print diff
        if diff:
            token_expired=1 #超时
        else:
            token_expired=0 #剩余时间多于1天
        return token_expired
               # print JsonDict['timestamp']
                #a=datetime.datetime.now()-JsonDict['timestamp']
                #print a.seconds
    def user_service_expire(self):
        t0 = datetime.datetime.now()
        # a=self.token_start+datetime.timedelta(minutes=120)
        #print t0,self.service_limitation,self.timestamp
        diff = t0 >= (self.timestamp + datetime.timedelta(days=self.service_limitation))  # 設置爲30days後失效
        #print diff
        if diff:
            service_expired = 1  # 超时
        else:
            service_expired = 0
        return service_expired