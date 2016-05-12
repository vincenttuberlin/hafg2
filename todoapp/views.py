from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader
from todoapp.forms import  ToDoForm
from django.core.urlresolvers import reverse,reverse_lazy
import django.http
from django.template import RequestContext
# Create your views here.
from .models import TodoItem

def index(request):
        todo_list = TodoItem.objects.all()
        template = loader.get_template('todoapp/index.html')
        context = {
            'todo_list': todo_list,
        }
        return HttpResponse(template.render(context,request))
def impressum(request):
        return render_to_response('todoapp/impressum.html')
def howto(request):
        return render_to_response('todoapp/howto.html')
def createtodo(request):
        if request.method=='GET':
            form = ToDoForm()
        else:
            form = ToDoForm(request.POST)
            if form.is_valid():
                description = form.cleaned_data['description']
                deadline = form.cleaned_data['deadline']
                progress = form.cleaned_data['progress']
                TodoItem.objects.create(description=description,deadline=deadline,progress=progress)
                return django.http.HttpResponseRedirect(reverse_lazy('index'))
        return render(request, 'todoapp/createtodo.html', {
            'form': form,
        })

def delete(request,id=None):
        try:

            TodoItem.objects.filter(id=id).delete()
            return django.http.HttpResponseRedirect(reverse_lazy('index'))
        except:
            raise django.http.Http404('Item does not exist')
def edit(request,id=None):
    editItem = None
    try:
        editItem = TodoItem.objects.get(id=id)
    except:
        raise django.http.Http404('Item does not exist')
    if request.method == 'GET':
        form = ToDoForm(instance=editItem)
        return render(request, 'todoapp/createtodo.html', {'form': form})
    else:
        form = ToDoForm(request.POST)
        if form.is_valid():
            editItem.description = form.cleaned_data['description']
            editItem.deadline = form.cleaned_data['deadline']
            editItem.progress = form.cleaned_data['progress']
            editItem.save()
            return django.http.HttpResponseRedirect(reverse_lazy('index'))
    return render(request, 'todoapp/createtodo.html', {
        'form': form,
    })

''' Missing:
def editTodo
def createTodo
def howTo'''

