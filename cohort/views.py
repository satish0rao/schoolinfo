# Create your views here.

from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def berkeley(request):
    return render(request,'cohort/graph.html',{})

def d3_chart(request):
    return render(request,'cohort/graph_d3.html',{})

def data(request,data_id):
    return render(request,'cohort/data'+data_id + '.tsv')

def catch(request,filename):
    return render(request,'cohort/'+ filename)
