from django.db import models
import uuid

# Create your models here.


class App(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(null=True,blank=True,upload_to='app_images/')
    up_coming = models.BooleanField(default=False)
    url_name = models.CharField(max_length=255, null=True, blank=True)

    def  __str__(self):
        return self.name


class Services(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(null=True,blank=True,upload_to='services_images/')

    def   __str__(self):
        return self.name

