from django.shortcuts import render
from main.models import TaskList
from django.http import JsonResponse
# Create your views here.


def task_lists(request):
    tasks = TaskList.objects.all()

    j_tasks = [t.x`() for t in tasks]

    return JsonResponse(j_tasks, safe=False)



def task_ls_detail(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(task_list.to_json(), safe=False)



def task(request, pk):
    try:
        tasklist = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = tasklist.task_set.all()
    json_tasks = [t.to_json() for t in tasks]
    return JsonResponse(json_tasks, safe=False)
