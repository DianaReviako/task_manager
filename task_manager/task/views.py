from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date
from .forms import TaskForm
from .models import Task


def create_task_view(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            deadline_date = task_form.cleaned_data["deadline_date"]
            text = request.POST.get("text")
            task = Task.objects.create(deadline_date=deadline_date, text=text)
            task.save()
            return redirect('actual_tasks')
        else:
            return HttpResponse("Invalid data")
    else:
        task_form = TaskForm()
        return render(request, 'create_task.html', {'form': task_form})


def actual_tasks_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        current_date = date.today()
        list_actual_tasks = []
        for task in tasks:
            if task.deadline_date >= current_date and not task.status:
                list_actual_tasks.append(task)
        return render(request, 'actual_tasks.html', context={'tasks': list_actual_tasks})
    if request.is_ajax() and request.method == 'POST':
        selected_list = request.POST.getlist('selected[]')
        for key in selected_list:
            if key.startswith('task'):
                task_id = int(key.split('task')[1])
                task = Task.objects.get(pk=task_id)
                print(task)
                task.status = True
                task.save()
        return HttpResponse('OK')
    print('you are loshara')

# def change_task_status(request):
#     if request.is_ajax() and request.method == 'POST':
#         selected_list = request.POST.getlist('selected[]')
#         for key in selected_list:
#             if key.startswith('task'):
#                 task_id = int(key.split('task')[-1])
#                 task = Task.objects.get(pk=task_id)
#                 task.status = True
#                 task.save()
#                 actual_tasks_view(request)
#     return redirect('actual_tasks')


def edit_task(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        edit_task_text = request.POST.get("text")
        edit_task_date = request.POST.get("deadline_date")
        task.text = edit_task_text
        task.deadline_date = edit_task_date
        task.save()
        return redirect('actual_tasks')
    else:
        task = Task.objects.get(id=pk)
        deadline = task.deadline_date
        text = task.text
        task_form = TaskForm(initial={'deadline_date': deadline, 'text': text})
        return render(request, 'edit_task.html', context={'task': task, 'form': task_form})


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('actual_tasks')
