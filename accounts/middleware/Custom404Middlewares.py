GREEN_BOLD = "\033[1;32m"
YELLOW_BOLD = "\033[1;33m"
RESET = "\033[0m"
print(f"{YELLOW_BOLD}LOADING CUSTOM 404 MIDDLEWARE FROM 'get_details.py'{RESET}")




# middleware.py
from django.urls import resolve, Resolver404
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin

class Custom404Middleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            resolve(request.path)  # Try to resolve the requested URL
        except Resolver404:
            return render(request, '404.html', status=404)  # Render custom 404 page



print(f"{GREEN_BOLD}****************************** CUSTOM MIDDLEWARE LOADED SUCCESSFULLY ******************************{RESET}")