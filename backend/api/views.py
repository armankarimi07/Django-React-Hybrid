import json

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from api.models import Employee
from api.serializers import EmployeeSerializer, LoginSerializer, SignupSerializer

# Create your views here.

def index(request):
    return render(request, "api/index.html")


class MyReactView(TemplateView):
    template_name = 'react_app.html'

    def get_context_data(self, **kwargs):
        return {'context_variable': 'value'}


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def get_queryset(self):
        # filter queryset based on logged in user
        return self.request.user.employees.all()

    def perform_create(self, serializer):
        # ensure current user is correctly populated on new objects
        serializer.save(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class EmployeeView(TemplateView):
    # our hybrid template, shown above
    template_name = 'api/index.html'

    def get_context_data(self, **kwargs):
        # passing the department choices to the template in the context
        return {'department_choices': [{ 'id': c[0], 'name': c[1]} for c in Employee.DEPARTMENT_CHOICES],}
    
    
def authenticate_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('api:index'))
        return render(request, "api/login.html", {'form': form})
    form = AuthenticationForm()
    return render(request, "api/login.html", {'form': form})


@extend_schema(request=SignupSerializer)
@api_view(['GET', 'POST'])
def signup_view(request: HttpRequest):
    if request.method == "GET":
        return Response({'message': "Enter username and password to signup"})
    
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = SignupSerializer(data=data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            User.objects.create(
                username = username,
                email = email,
                password = password
            )
            return JsonResponse("OK")
        print(serializer.errors)
        return JsonResponse("error")
    
    
class SignupView(APIView):
    serializer_class = SignupSerializer
    
    def get(self, request):
        return Response({'message': "Send username and password"})
        
    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(
                username=serializer.validated_data.get('username'),
                password=serializer.validated_data.get('password')
            )
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
        
        
@require_POST
def login_view(request):
    data = json.loads(request.body)
    print("DATA", data)
    username = data.get('username')
    password = data.get('password')
    print("USERNAME and PASSWORD: ", username, password)
    if username is None or password is None:
        return JsonResponse({"details": "Please provide username and password"})
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"details": "Successfully logged in"})
    else:
        print("USER NOT FOUND")
        return JsonResponse({"details": "Invalid credentials"}, status=400)


def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"details": "You are not logged in"}, status=400)
    logout(request)
    return JsonResponse({"details": "Successfully logged out"})


@ensure_csrf_cookie
def session_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"isauthenticated": False})
    return JsonResponse({"isauthenticated": True})


def whoami_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"isauthenticated": False})
    return JsonResponse({"username": request.user.username})