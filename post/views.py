from __future__ import unicode_literals
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post,Reply
# Create your views here.
def wall(request):
	return render(request,'hello.html',{'name': request.session['email']})