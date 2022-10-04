from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def ajax(request):
    data = {"arr":[
        {"id": 1, "name": "Alex"},
        {"id":2,"name":"Vasya"}]}
    return JsonResponse(data)


def get_page(request):
    return render(request, 'page1.html')
