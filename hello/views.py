from django.http import HttpResponse


def helloworld(request):
    return HttpResponse("<h1>Hello World!</h1>")