from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth import hashers
from django.http import JsonResponse
from django.urls import reverse

User = get_user_model()   # ensures compatibility with custom user models

class LoginAdmin(View):
    def get(self, request):
        return render(request, 'home06.html')

    def post(self, request):
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        # Authenticate user
        user = authenticate(username=username, password=password)
        errors = {}
        if user is not None:
            login(request, user)
            request.session['signin'] = 'on'
            request.session.set_expiry(345600)  # Set session expiry to 345600 seconds (4 days)
            return JsonResponse({"success": True})
        else:
            errors['login'] = "Invalid username or password"
            if errors:
                return JsonResponse({"errors": errors}, status=400)
            
            
            #return render(request, 'home06.html', {'password': 'on'})


class LogoutAdmin(View):
    def get(self, request):

        logout(request)  
        return redirect('home')  
    
    
