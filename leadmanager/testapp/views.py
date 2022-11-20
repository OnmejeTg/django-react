from django.shortcuts import render

# Create your views here.

def index(request):
    print(dir(request))
    context = {}
    return render(request, 'testapp/index.html', context=context)
