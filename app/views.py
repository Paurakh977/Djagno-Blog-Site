from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from app.models import Task
def home(request):
    success=False
    if request.method=='GET':
        total=request.GET.get('total')
        success=request.GET.get('success')
        context={'total':total,'success':success}
    return render(request,'home.html',context)

def register(request):
    success = False
    if request.method == 'POST':
        task = request.POST.get('task')
        desc = request.POST.get('desc')
        if task and desc:
            obj = Task(task=task, desc=desc)
            obj.save()
            no_of_obj=Task.objects.count()
            # redirect garda jaile suru ma /
            url=f'/home?total={no_of_obj}&success={True}'
            return redirect(url)
    return render(request, 'register.html')

def todo(request):
    tasks=Task.objects.all()
    context={'tasks':tasks}
    return render(request,'todo.html',context)

def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    task.delete()
    return redirect('/todo')

def update(request,task_id,task_name,task_desc):
    context = {
        'task_name': task_name,
        'task_desc': task_desc
    }
    if request.method == 'POST':
        newtask = request.POST.get('task')
        newdesc = request.POST.get('desc')
        if newtask and newdesc:
            task=Task.objects.get(id=task_id)
            task.task=newtask
            task.desc=newdesc
            task.save()
            return redirect('/todo')


    return render(request, 'update.html', context)