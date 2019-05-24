from django.shortcuts import render
from tcapp.forms import InfoForm
from tcapp.models import User
from django.views.generic import TemplateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    form = InfoForm()
    if request.method == 'POST':
        form = InfoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print('ERROR FORM INVALID')

    context = {'form':form}
    return render (request,'registration/signup.html',context)

class DetailPage(TemplateView,LoginRequiredMixin):
    template_name = 'registration/detail.html'

class InfoDetail(DetailView,LoginRequiredMixin):
    context_object_name = "info_detail"
    model = User
    template_name = "registration/info_detail.html"

class InfoUpdate(UpdateView,LoginRequiredMixin):
    model = User
    fields = ('username','first_name','last_name','email','age','gender','color')
    template_name = 'registration/info_form.html'

class InfoDelete(DeleteView,LoginRequiredMixin):
    model = User
    template_name = 'registration/info_delete.html'
    success_url = reverse_lazy('index')
