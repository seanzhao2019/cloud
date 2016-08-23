from __future__ import unicode_literals

from django.db import models

# Create your models here.
class NodeInfo(models.Model):
    node_mac=models.CharField(max_length=8)
    node_user=models.CharField(max_length=30)
    cloud_mac=models.CharField(max_length=8)
    service_limitation = models.IntegerField()
    timestamp=models.DateTimeField()
    class Meta:
        unique_together=(("node_mac", "node_user"),)

    def __unicode__(self):
        return self.node_mac

class TokenTable(models.Model):
    node=models.OneToOneField(NodeInfo)
    token=models.CharField(max_length=32,unique=True)
    priority=models.IntegerField()
    service_type=models.IntegerField()
    service_limitation=models.IntegerField()
    token_start=models.DateTimeField(auto_now=True)
    token_security_level=models.CharField(max_length=20)
    timestamp=models.DateTimeField()

    def __unicode__(self):
        return unicode(self.node)

