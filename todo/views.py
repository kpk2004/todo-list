from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.template import loader
from .models import todolist
class Myform(forms.Form):
    task=forms.CharField(max_length=100)
# Create your views here.
def whattodo(request):
    template = loader.get_template("todo/whattodo.html")
    todolistshow=todolist.objects.all().values()
    if request.method=="POST":
        form=Myform(request.POST)
        if form.is_valid():
            t=todolist(todo=form.cleaned_data['task'])
            t.save()
            return HttpResponseRedirect('/todo/')
    else:
        form=Myform()
    return render(request,'todo/whattodo.html', {'form': form,'todolistshow': todolistshow})
def edit(request):
    template = loader.get_template("todo/edit.html")
    todolistshow=todolist.objects.all().values()
    lst=[]
    return render(request,'todo/edit.html', {'todolistshow': todolistshow,'lst':lst})
def delete(request,id):
    template = loader.get_template("todo/edit.html")
    to=todolist.objects.get(id=id)
    to.delete()
    return HttpResponseRedirect('/todo/edit/')