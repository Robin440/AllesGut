# Django imports
from django.shortcuts import render,redirect


# Utils imports
from utils.validators import is_valid_email,check_password_for_spaces
from utils.utils_generator import  generate_random_string
from utils.get_details import get_member,get_member_image

# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


from django.contrib.gis.geoip2 import GeoIP2

class IPAddressView(APIView):

    def get(self, request, *args, **kwargs):
        """
        Handle GET request
        """
        return render(request, 'my_ip.html')

    def post(self, request, *args, **kwargs):
        """
        Handle POST request
        """

        print(f" geoip2 = {GeoIP2}")
        try:
            x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
            if x_forwarded_for:
                ip = x_forwarded_for.split(",")[0]
            else:
                ip = request.META.get("REMOTE_ADDR")
            g = GeoIP2()
            try:
                geo_data = g.city(ip)
                return render(request, "my_ip.html", {"response": geo_data})
            except Exception as e:
                return render(request, "my_ip.html", {"response": str(e)})
        except Exception as e:
            return render(request, "my_ip.html", {"response": str(e)})