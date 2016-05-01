#coding=utf-8
#__author__='zhao'
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from fognode.models import NodeInfo, TokenTable
from datetime import datetime, date
import hashlib
import datetime
# Create your views here.

PRIORITY = 5 #1-5，level 1 need to be handled firstly
SERVICE_TYPE = 0#0==nothing
SERVICE_LIMITATION=30 #30 DAYS
TOKEN_EXPIRE=1 #1 DAY

class Check_validity(object):
    def __init__(self,timestamp,time_limitation):
        self.timestamp=timestamp
        self.time_limitation=time_limitation

    def check_time_limitation(self):
        t0=datetime.datetime.now()
        diff=t0-self.timestamp
        #print diff
        if diff.seconds>2000:
            status=1 #超时
        else:
            status=0 #剩余时间多于1天
        return status
               # print JsonDict['timestamp']
                #a=datetime.datetime.now()-JsonDict['timestamp']
                #print a.seconds 


@csrf_exempt
def Register_NodeInfo(request):

    try:
        if request.method=='POST':
            #print request.POST

            node_mac_get=request.POST.get('node_mac')
            node_user_get=request.POST.get('node_user')
            cloud_mac_get=request.POST.get('cloud_mac')

            #token_priority_get=request.POST.get('token_priority')
            #token_service_type_get=request.POST.get('token_service_type')
            #token_time_limitation_get=request.POST.get('token_time_limitation')
            #print type(token_time_limitation_get),type(node_mac_get)
            #print [token_time_limitation_get,token_priority_get,token_service_type_get]
                #print type(token_time_limitation_get)
            get_create_nodeinfo=NodeInfo.objects.get_or_create(node_mac=node_mac_get,node_user=node_user_get,
                                                               defaults={'cloud_mac':cloud_mac_get})
                #print create_nodeinfo
                #print dir(create_nodeinfo)
                #print hasattr(create_nodeinfo,'pk')
            node_pk=get_create_nodeinfo[0].pk
            create_time=datetime.datetime.now()
            create_time_str=create_time.strftime("%Y-%m-%d %H:%M:%S")
            #print type(create_time)
            if get_create_nodeinfo[1]:
                m = hashlib.md5()
              #print type(fog_mac_get),type(node_mac_get)
                m.update(node_mac_get+node_user_get+create_time_str)
                token=m.hexdigest()
                print token
            #print node_id

                create_token=TokenTable()
            #print dir(create_token)
                create_token.node_id=node_pk
                create_token.token=token
                create_token.priority=PRIORITY
                create_token.service_type=SERVICE_TYPE
                create_token.service_limitation=create_time+datetime.timedelta(days=SERVICE_LIMITATION)
                create_token.save()
                JsonDict={"token":token,"priority":PRIORITY,"service_type":SERVICE_TYPE,
                             "service_limitation":create_token.service_limitation,'timestamp':create_token.timestamp,
                          "token_start":create_token.token_start,"status":0
                             }
            else:
                node=TokenTable.objects.get(node_id=node_pk)
                print node,type(node)
                node_token=node.token
                node_priority=node.priority
                node_service_type=node.service_type
                node_service_limitation=node.time_limitation
                node_timestamp=node.timestamp
                check=Check_validity(node_timestamp,node_time_limitation)
                check_status=check.check_time_limitation()
                print check_status
                if check_status == 0:
                    JsonDict={"token":node_token,"priority":node_priority,"service_type":node_service_type,
                             "time_limitation":node_service_limitation,'timestamp':node_timestamp
                             }
                else:
                    JsonDict={'status':check_status}
            print JsonDict
        return JsonResponse(JsonDict)

    except:
        print 'something wrong'

    return HttpResponse('ERROR')