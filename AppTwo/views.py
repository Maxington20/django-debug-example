from django.shortcuts import render

# Added this
# from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request, 'apptwo/index.html')

def help(request):
    myContent = {'content': 'Help Page'}

    return render(request, 'apptwo/help.html',context=myContent)

def user(request):
    userList = User.objects.order_by('LastName')
    users = {'users' : userList}
    return render(request,'apptwo/users.html',context=users)

    # form = NewUserForm()

    # if request.method == 'POST':
    #     form = NewUserForm(request.POST)

    #     if form.is_valid():
    #         form.save(commit=True)
    #         return index(request)
    #     else:
    #         print('Error. form invalid')
    # return render(request,'apptwo/users.html',{'form':form})