from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime

class GoodMorningView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"goodmorning"})
class GoodAfternoonview(APIView):
    def get(self,request,*args,**kwargs):
        return Response({"msg":"goodafternoon"})
class GreetingView(APIView):
    def get(self,request,*args,**kwargs):
        cur_date=datetime.now()
        c_hour=cur_date.hour
        greetings=""
        if c_hour<12:
            greetings="Good morning"
        elif c_hour<18:
            greetings="Good afternoon"
        elif c_hour<24:
            greetings="Good evening"
        return Response({"msg:greetings"})


