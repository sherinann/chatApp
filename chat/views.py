from django.shortcuts import render
from django.http import HttpResponse
from chat.forms import UserForm
from django.contrib.auth.models import User
from .models import UserMessageInfo
from django.contrib import auth
import sqlite3
from django.http import HttpResponseRedirect
from django.template import  RequestContext
from django.contrib.auth import authenticate,login
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils import timezone
import datetime
# Create your views here.

def AddUser(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            new_user=User.objects.create_user(**form.cleaned_data)
            login(request,new_user)
            return HttpResponseRedirect('/chat')
    else:
        form=UserForm()
    return render(request,'chat/login/signup.html',{'form':form})


def Login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/chat')
        else:
           return HttpResponseRedirect('/chat/login')

    return render(request, 'chat/login/login.html', {})

def Message(request):
    if request.method=="POST":
        receiver=request.POST['receiver']
        message=request.POST['message']
        if User.objects.filter(username=receiver).exists():
            print("in")
            new=UserMessageInfo(sender=auth.get_user(request).username,receiver=receiver,message=message)
            new.save()
            return HttpResponseRedirect('/chat')
        else:
              return HttpResponseRedirect('/chat/messages')
    return render(request, 'chat/messages/message.html', {})

def Chats(request):              
    if request.method=="GET":
        chat_names = []
        username=auth.get_user(request).username
        info=UserMessageInfo.objects.filter(receiver=username).values_list('sender',flat=True)
        for i in info:
            if i not in chat_names:
                chat_names.append(i)
        info2=UserMessageInfo.objects.filter(sender=username).values_list('receiver',flat=True)
        for i in info2:
            if i not in chat_names:
                chat_names.append(i)
        print(chat_names)
        return render(request, 'chat/messages/chats.html', {'people':chat_names})
    return render(request, 'chat/messages/chats.html', {})

def ChatSpecific(request):
    if request.method=="GET":
        user=request.GET['']
    return render(request,'chat/messages/chat_specific.html',{})

def index(request):
    return HttpResponse("chat app")