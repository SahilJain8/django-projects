from django.shortcuts import render
from django.http import HttpResponse,response




class Home():

    def index(request):
        return render(request, "index.html")


    def index_home(request):
           
        return render(request, "index.html")