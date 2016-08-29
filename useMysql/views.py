#coding=utf-8
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
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