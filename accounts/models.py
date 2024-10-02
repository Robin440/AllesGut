from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class VerificationToken(models.Model):
    uuid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    token = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    otp = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f'{self.otp} - {self.name}'



class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)  # Custom username field
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150,null=True,blank=True)
    is_active = models.BooleanField(default=False)
    is_password =  models.BooleanField(default=False)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_superadmin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    verification = models.ForeignKey(VerificationToken, on_delete=models.SET_NULL, null=True, blank=True, related_name="user_verification")



    USERNAME_FIELD = 'email'  # Use email for authentication
    REQUIRED_FIELDS = ['username']  # Make username a required field

    def __str__(self):
        return self.email







