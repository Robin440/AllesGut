# Django imports
from django.shortcuts import render,redirect
from django.contrib.auth.models import AnonymousUser    


# Utils imports
from utils.validators import is_valid_email,check_password_for_spaces
from utils.utils_generator import  generate_random_string
from utils.get_details import get_member,get_member_image

# Rest framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


# Import Serializers
from my_ip.serializers import MyIPCreateSerializers,MyIPListSerializers


# model import
from my_ip.models import MyIP
from django.core.paginator import Paginator


from django.contrib.gis.geoip2 import GeoIP2

class IPHomeView(APIView):

    def get(self, request, *args, **kwargs):
        """
        Handle GET request
        """
        return render(request, 'my_ip_home.html')


class FindMyIPAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """
        Handle GET request
        """
        context = {}
        context['get']="Required"
        return render(request, 'my_ip.html',context)

    def post(self, request, *args, **kwargs):
        """
        Handle POST request
        """
        context = {}
        context['post']="Required"
        try:
            x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
            if x_forwarded_for:
                ip = x_forwarded_for.split(",")[0]
            else:
                ip = request.META.get("REMOTE_ADDR")
            g = GeoIP2()
            try:
                geo_data = g.city(ip)
                print(f"geo_data -  {geo_data}")
                try:
                    context = geo_data
                    member = get_member(request.user)
                    context['member'] = member.uuid
                    context['ip'] = ip
                    serializer = MyIPCreateSerializers(data = context)
                    if serializer.is_valid():
                        serializer.save()
                        return render(request,"my_ip.html",context)
                    context['error']=str(serializer.errors)
                    return render(request,'my_ip.html',context)
                except Exception as e:
                    print(f'error -  {e}')
                return render(request, "my_ip.html", context)
            except Exception as e:
                return render(request, "my_ip.html", {"response": str(e)})
        except Exception as e:
            return render(request, "my_ip.html", {"response": str(e)})


class IPHistoryAPIView(APIView):
    """_summary_

    Args:
        APIView (_type_): _description_
    """
    def get(self, request, *args, **kwargs):
        """Handles fetching IP data with filters and pagination."""

        context = {}
        user = request.user
        print(f"user = {user}")
        if isinstance(user, AnonymousUser):
            context['error']="Session time out.Please login again."
            return render(request,'login.html',context)

        member = get_member(user)

        # Fetch all IP data for the logged-in user
        ip_data = MyIP.objects.filter(member=member)

        # Get filter options from unique values in the database
        countries = ip_data.values_list('country_name', flat=True).distinct()
        regions = ip_data.values_list('region', flat=True).distinct()
        cities = ip_data.values_list('city', flat=True).distinct()
        dates = ip_data.values_list('created_at', flat=True).distinct()

        # Add filter logic (optional, you can refine based on the user's filter choices)
        country_filter = request.GET.get('country')
        region_filter = request.GET.get('region')
        city_filter = request.GET.get('city')
        date_filter = request.GET.get('date')

        if country_filter:
            ip_data = ip_data.filter(country_name=country_filter)
        if region_filter:
            ip_data = ip_data.filter(region=region_filter)
        if city_filter:
            ip_data = ip_data.filter(city=city_filter)
        if date_filter:
            ip_data = ip_data.filter(created_at__date=date_filter)

        # Paginate the IP data, showing 7 records per page
        paginator = Paginator(ip_data, 7)  # Show 7 rows per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Add data and filters to the context
        context['ip_data'] = page_obj
        context['countries'] = countries
        context['regions'] = regions
        context['cities'] = cities
        context['dates'] = dates

        return render(request, 'my_ip_histories.html', context)
