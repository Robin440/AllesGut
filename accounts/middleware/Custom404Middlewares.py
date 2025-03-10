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
