"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import NewProjectForm
from .models import Project
from .models import ProjectType
from .models import Account
from .models import Skill
from django.views.decorators.csrf import csrf_exempt

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year, 
        }
    )
@csrf_exempt
def newproject(request):
    assert isinstance(request, HttpRequest)
    if request.method == 'POST':
        form = NewProjectForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'app/index.html',{})
    else:
        return render(
            request,
            'app/newproject.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
            }
        )

def myprojects(request):
    assert isinstance(request, HttpRequest)
    all_project = Project.objects.all()
    return render(
        request,
        'app/myprojects.html',
        {
            'title':'Home Page',
            'year':datetime.now().year, 
            'all':all_project
        }
    )

def viewprojects(request):
    assert isinstance(request, HttpRequest)
    project_data = Project.objects.all()
    return render(
        request,
        'app/viewprojects.html',
        {
            'title':'Home Page',
            'year':datetime.now().year, 
            'data':project_data
        }
    )

def contactapp(request, Account_ID):
    assert isinstance(request, HttpRequest)
    all_account = Account.objects.get(AccountID = Account_ID)
    return render(
        request,
        'app/contactapp.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'Account':all_account
        }
    )

def viewapplicants(request, Project_ID):
    assert isinstance(request, HttpRequest)
    all_project = Project.objects.get(ProjectID = Project_ID) # https://www.youtube.com/watch?v=hyzM1lpc6Rs&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=45
    applicants = Account.objects.all()
    appdata = list(applicants.values_list('SkillID', flat=True))
    prodata = list(all_project.ProjectTypeID.SkillID.values_list('SkillID', flat=True))
    app1 = appdata[0:4]
    app2 = appdata[4:8]
    app3 = appdata[8:12]
    app4 = appdata[12:16]
    app5 = appdata[16:20]
    app6 = appdata[20:24]
    app7 = appdata[24:28]
    app8 = appdata[28:32]
    applicant1 = Account.objects.get(AccountID=1)
    applicant2 = Account.objects.get(AccountID=2)
    applicant3 = Account.objects.get(AccountID=3)
    applicant4 = Account.objects.get(AccountID=4)
    applicant5 = Account.objects.get(AccountID=5)
    applicant6 = Account.objects.get(AccountID=6)
    applicant7 = Account.objects.get(AccountID=7)
    applicant8 = Account.objects.get(AccountID=8)
    gate1 = False
    gate2 = False
    gate3 = False
    gate4 = False
    gate5 = False
    gate6 = False
    gate7 = False
    gate8 = False
    for data in app1:
        if data in prodata:
            gate1 = True
    for data in app2:
        if data in prodata:
            gate2 = True
    for data in app3:
        if data in prodata:
            gate3 = True
    for data in app4:
        if data in prodata:
            gate4 = True
    for data in app5:
        if data in prodata:
            gate5 = True
    for data in app6:
        if data in prodata:
            gate6 = True
    for data in app7:
        if data in prodata:
            gate7 = True
    for data in app8:
        if data in prodata:
            gate8 = True
   
    

    return render(
        request,
        'app/viewapplicants.html',
        {
            'title':'Home Page',
            'year':datetime.now().year, 
            'all':all_project,
            'applicants':applicants,
            'appdata':appdata,
            'prodata':prodata,
            'app1':app1,
            'app2':app2,
            'app3':app3,
            'app4':app4,
            'app5':app5,
            'app6':app6,
            'app7':app7,
            'app8':app8,
            'applicant1':applicant1,
            'applicant2':applicant2,
            'applicant3':applicant3,
            'applicant4':applicant4,
            'applicant5':applicant5,
            'applicant6':applicant6,
            'applicant7':applicant7,
            'applicant8':applicant8,
            'gate1':gate1,
            'gate2':gate2,
            'gate3':gate3,
            'gate4':gate4,
            'gate5':gate5,
            'gate6':gate6,
            'gate7':gate7,
            'gate8':gate8,
        }
    )

def application(request, Project_ID):
    assert isinstance(request, HttpRequest)
    all_project = Project.objects.get(ProjectID = Project_ID)
    return render(
        request,
        'app/application.html',
        {
            'title':'Home Page',
            'year':datetime.now().year, 
            'all':all_project,
        }
    )



def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
