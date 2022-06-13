from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

dics=[
    {'id':1,
     'name':'Voyage au vent',
     'description':"c'est le roman du bonheur de Smart"
     },
    {
     'id':2,
     'name':'amour flottant',
     'description':"de l'amoour sous un serisier waooh"
    },
    {'id':3,
     'name':'le banquer de la vie',
     'description':"Receuil de la vie de Charles le roy"}
]
author="Smart Romaric"
context={'oeuvre':dics,'auteur':author}
def project(request):
    return render(request ,'project/single_project.html',context)

def projects(request,pk):
    livre=None
    for elt in dics:
        if elt['id'] ==pk:
            livre=elt
    return render(request ,'project/projects.html',{'livre':livre})
