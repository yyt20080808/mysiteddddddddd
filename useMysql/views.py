#coding=utf-8
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file
# Create your views here.
@csrf_exempt
def login_auth(request):
    if request.method == 'POST':
        print "start"
        a = request.POST.get('username')
        b = request.POST.get('password')
        user = authenticate(username=a,password=b)
        if user != None :
            login(request, user)
            return JsonResponse({"returnInfo": 'authed'})
        else:
                return JsonResponse({"returnInfo": 'password not right'})
    else:
        print "sssss"
        return JsonResponse({"returnInfo": 'sorry,you haven\'t login'})
        # return render(request,'news/column.html',{'column':column})
@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({"returnInfo": 'logout'})



@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            print "start upload!"
            return HttpResponseRedirect('/file/success/')

    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)