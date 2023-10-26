from django.shortcuts import render, redirect
from .models import task
from .form import todo_form
# Create your views here.
def add(request):
    task1 = task.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')

        t = task(name=name, priority=priority,date=date)
        t.save()
    return render(request,'index.html',{'task1':task1})
# def detail(request):
#
#     return render(request,'detail.html',)
def delete(request,taskid):
    task2= task.objects.get(id=taskid)
    if request.method=='POST':
        task2.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    t=task.objects.get(id=id)
    form=todo_form(request.POST or None,instance=t)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'form':form,'t':t})