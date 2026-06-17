from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request, "home.html")

def result(request):
    num1 = int(request.GET.get('number1'))
    num2 = int(request.GET.get('number2'))

    
    if request.GET.get('add') == "":
        ans = num1 + num2

    elif request.GET.get('subtract') == "":
        try:
            num1 = float(num1)
            num2 = float(num2)
            ans = num1 - num2
        except ValueError:
            return HttpResponse("Invalid input: num1 and num2 must be numbers.", status=400)

    elif request.GET.get('multiply') == "":    
        ans = num1 * num2

    else:
        ans = num1 / num2

    return render(request,'result.html',{'ans': ans})
