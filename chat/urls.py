from django.conf.urls import url

from . import  views

urlpatterns=[
    url(r'^$',views.index,name="index"),
    url(r'^signup',views.AddUser,name="signup"),
    #url(r'^logout',views.Logout,name="logout"),
    url(r'^login', views.Login, name="login"),
    url(r'^message', views.Message, name="new_message"),
    url(r'^chats', views.Chats, name="chats"),
    url(r'^chat_specific', views.ChatSpecific, name="chatSpecific"),

]