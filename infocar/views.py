from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView
from .forms import AddFormAuto, FilterAutoForm
from .models import Auto, Transmission, Complectation,Engine
from django.shortcuts import render, get_object_or_404, redirect


def index(request):
    t = Transmission.objects.all()
    all_car = Auto.objects.all()
    complect = Complectation.objects.all()

    if request.method == 'POST':
        form = FilterAutoForm(request.POST)
        if form.is_valid():
            url = f'/filter/{Engine.objects.get(pk=request.POST["engine"]).slug}/{Transmission.objects.get(pk=request.POST["transmission"]).slug}'
            return redirect(url)
    else:
        form = FilterAutoForm()

    return render(request, 'infocar/index.html', {'all_car': all_car, 't': t, 'complect': complect,'form':form})

def filter_post(request,trans_slug,engine_slug):
    trans = Transmission.objects.get(slug=trans_slug).pk
    eng = Engine.objects.get(slug=engine_slug).pk
    filter_car = Auto.objects.filter(transmission_id=trans,engine_id=eng)
    if request.method == 'POST':
        form = FilterAutoForm(request.POST)
        if form.is_valid():
            url = f'/filter/{Engine.objects.get(pk=request.POST["engine"]).slug}/{Transmission.objects.get(pk=request.POST["transmission"]).slug}'
            return redirect(url)
    else:
        form = FilterAutoForm()
    return render(request,'infocar/filters.html',{'filter_car': filter_car,'form':form})

class CreateAuto(CreateView):
    model = Auto
    form_class = AddFormAuto
    template_name = 'infocar/create.html'
    success_url = '/'


class UpdateAuto(UpdateView):
    model = Auto
    template_name = 'infocar/edit.html'
    form_class = AddFormAuto


class DeleteAuto(DeleteView):
    model = Auto
    success_url = '/'
    template_name = 'infocar/index.html'


def get_mechanical(request, id):
    trans = Transmission.objects.get(id=id)
    res = trans.auto_set.all()
    t = Transmission.objects.all()
    return render(request, 'infocar/filters.html', {'res': res, 't': t})


def get_post(request, post_slug):
    post = get_object_or_404(Auto,slug=post_slug)  # смотрит есть ли в модели Auto pk
    return render(request, 'infocar/post.html', {'post': post})

def get_filter(request):


    return render(request,'infocar/filt.html')
# def create_auto(request):
#     e = Engine.objects.all()
#     t = Transmission.objects.all()
#     if request.method == 'POST':
#         r = request.POST
#         try:
#             Auto.objects.create(
#                 firm=r['firm'],
#                 model=r['model'],
#                 color=r['color'],
#                 volume=r['volume'],
#                 price=r['price'],
#                 engine_id=r['engine'],
#                 transmission_id = r['transmission']
#             )
#             return HttpResponseRedirect('/')
#         except:
#             redirect('/infocar/create.html')
#     return render(request,'infocar/create.html',{'e':e,'t':t})

# def edit_auto(request,id):
#     e = Engine.objects.all()
#     t = Transmission.objects.all()
#     ed_auto = Auto.objects.get(id=id)
#
#     if request.method == 'POST':
#         r = request.POST
#         print(r)
#         try:
#             Auto.objects.filter(id=id).update(
#                 firm=r['firm'],
#                 model=r['model'],
#                 color=r['color'],
#                 volume=r['volume'],
#                 price=r['price'],
#                 engine_id=r['engine'],
#                 transmission_id = r['transmission']
#             )
#             return HttpResponseRedirect('/')
#         except:
#             redirect('/infocar/edit.html')
#         redirect('/infocar/index.html')
#     return render(request,'infocar/edit.html',{'e':e,'t':t,'ed_auto':ed_auto})
#
# def delete_auto(request,id):
#
#     if request.method == 'POST':
#         del_auto = Auto.objects.filter(id=id)
#         del_auto.delete()
#         return HttpResponseRedirect('/')