"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


# # In your main urls.py file
# from django.conf.urls import handler404,handler500
# from django.shortcuts import render

# def custom_404_view(request, exception):
#     return render(request, '404.html', status=404)

# def custom_500_view(request):
#     return render(request, '500.html', status=500)
    

# # Use the custom 404 view
# handler404 = 'core.urls.custom_404_view'

# # Use the custom 404 view
# handler500 = 'core.urls.custom_500_view'




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


