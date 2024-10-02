from django.db import models
import uuid
from member.models import Member

# Create your models here.



class MyIP(models.Model):
    uuid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    member =  models.ForeignKey(Member,on_delete=models.CASCADE,related_name='ip_member')    
    ip = models.CharField(max_length=20)
    longitude  = models.CharField(max_length=255,null=True,blank=True)
    latitude = models.CharField(max_length=255,null=True,blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)
    country_code =  models.CharField(max_length=255,null=True,blank=True)
    region = models.CharField(max_length=255,null=True,blank=True)
    region_code = models.CharField(max_length=255,null=True,blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    continent =  models.CharField(max_length=255,null=True,blank=True)
    continent_code =  models.CharField(max_length=255,null=True,blank=True)
    dma_code = models.CharField(max_length=255,null=True,blank=True)
    in_european_union = models.BooleanField(default=False)
    postal_code = models.CharField(max_length=255,null=True,blank=True)
    time_zone = models.CharField(max_length=255,null=True,blank=True)
    accurancy_radius =  models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)




    def  __str__(self):
        return self.member.user.email
 
