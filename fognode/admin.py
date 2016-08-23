from django.contrib import admin
from fognode.models import NodeInfo, TokenTable
# Register your models here.
class NodeInfoAdmin(admin.ModelAdmin):
    list_display = ('node_mac','node_user','cloud_mac','service_limitation','timestamp')
class TokenTableAdmin(admin.ModelAdmin):
    list_display = ('node','token','priority','service_type','service_limitation','token_security_level','token_start','timestamp')

admin.site.register(NodeInfo, NodeInfoAdmin)
admin.site.register(TokenTable, TokenTableAdmin)
#admin.site.register(NodeData, NodeDataAdmin)