from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.


def index(request):
	to=Todo.objects.all()
	if request.method=='POST':
		new_todo=Todo(
			title=request.POST['title'],
			age=request.POST['age']
			)
		new_todo.save()
		return redirect('/')
	return render(request,"index.html",{"todo":to})

def about(request):
	return render(request,"about.html")	