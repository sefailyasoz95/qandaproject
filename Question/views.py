from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse, HttpResponseRedirect


