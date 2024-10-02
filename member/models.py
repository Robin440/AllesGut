from django.db import models

# Create your models here.
from accounts.models import User
import uuid
from datetime import datetime
from django.utils import timezone

class Role(models.Model):
    uuid = models.UUIDField(primary_key=True,editable=True,default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name



class Member(models.Model):
    """
    models for handling  member information

    """
    uuid = models.UUIDField(primary_key= True,default= uuid.uuid4)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=200,null=True,blank=True)
    role = models.ForeignKey(Role,on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by',null=True,blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_by',null=True,blank=True)

    def __str__(self):
        return self.user.email
  


class MemberImage(models.Model):
    """_summary_ : Model for store member images

    """
    uuid = models.UUIDField(primary_key= True,default= uuid.uuid4)
    member = models.ForeignKey(Member, on_delete=models.CASCADE,related_name='memberimage_set')
    image = models.ImageField(upload_to='member_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.member.user.email




    