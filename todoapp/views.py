from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from .models import TodoItem

def index(request):
        todo_list = TodoItem.objects.all()
        template = loader.get_template('todoapp/index.html')
        context = {
            'todo_list': todo_list,
        }
        return HttpResponse(template.render(context,request))

def createtodo(request):
        template = loader.get_template('todoapp/createtodo.html')
        context = null

        return HttpResponse(template.render(context,request))
