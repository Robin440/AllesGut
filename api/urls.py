
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import user_views
# Importing views from apps
from accounts.views import user_views
from my_ip.views import ip_views


urlpatterns = [

    # accounts urls
    path('api-auth/', include('rest_framework.urls')),

    # Accounts urls
    path('',user_views.LoginView.as_view(),name='user_login'),
    path('api/login/',user_views.LoginView.as_view(),name='user_login'),
    path('api/logout/',user_views.LogoutAPIView.as_view(),name='user_logout'),
    path('api/register/',user_views.RegisterAPIView.as_view(),name='user_register'),
    path('api/home/',user_views.HomeListAPIView.as_view(),name='user_home'),
    path('api/verify/',user_views.VerifyMailLinkAPIView.as_view(),name='verify_mail'),
    path('api/verify_user/',user_views.OTPVerifyAPIView.as_view(),name='otp_verify'),
    path('api/resend_verification/',user_views.ResendVerificationAPIView.as_view(),name='resend_verification'),

    #  My IP urls
    path('api/ip_home/',ip_views.IPHomeView.as_view(),name='ip_home'),
    path('api/ip_history/',ip_views.IPHistoryAPIView.as_view(),name='ip_history'),
    path('api/my_ip/',ip_views.FindMyIPAPIView.as_view(),name='my_ip')



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

