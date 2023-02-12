from django.shortcuts import render, get_object_or_404
from .models import Agent, Management, Other
from .forms import Morning, Afternoon

# Create your views here.


def index(request):
    return render(request, 'staff/index.html')

def agent_list(request):
    agents = Agent.objects.all()

    return render(request, 'staff/agents/list.html',
            {'agents': agents})


def agent_detail(request, id):
    agent = get_object_or_404(Agent, id=id)

    return render(request, 'staff/agents/detail.html',
            {'agent': agent})

def management_list(request):
    management = Management.objects.all()

    return render(request, 'staff/management/list.html',
            {'management': management})

def management_detail(request, id):
    management = get_object_or_404(Management, id=id)

    return render(request, 'staff/management/detail.html',
            {'management': management})

def other_list(request):
    other_staff = Other.objects.all()

    return render(request, 'staff/others/list.html',
            {'other_staff': other_staff})

def other_detail(request, id):
    other_staff = get_object_or_404(Other, id=id)

    return render(request, 'staff/others/detail.html',
            {'other_staff': other_staff})

def timetable_generator(request):
    if request.method == 'POST':
        
        form1 = Morning(request.GET)
        if form1.is_valid():
            form1.save()
        
        form2 = Afternoon(request.GET)
        if form2.is_valid():
            form2.save()

    else:
        form1 = Morning()
        form2 = Afternoon()

    return render(request, 'staff/timetable-generator.html',
            {'form1': form1, 'form2': form2})



