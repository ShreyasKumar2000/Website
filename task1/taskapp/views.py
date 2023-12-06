

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from . models import project
def demo(request):
    obj=project.objects.all()
    return render(request,"index.html",{'info':obj})

# def arithmetic(request):
#     return render(request,"arithmeticoper.html")
#
# def contact(request):
#     return render(request,"contact.html")
#
# def details(request):
#     return render(request,"details.html")
#
# def endpage(request):
#     return HttpResponse("You have Exit from page.")
#
# def operation1(request):
#     a=int(request.GET['num1'])
#     b= int(request.GET['num2'])
#     res1=a+b
#     res2=a-b
#     res3=a*b
#     res4=a/b
#     return render(request,"operations.html",{'add':res1,'subtract':res2,'multiply':res3,'divide':res4})
