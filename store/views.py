from django.views import generic
from .models import bijou,sub_bijou
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView,UpdateView,DeleteView

class StoreView(generic.ListView):
    template_name = 'store/index.html'
    context_object_name = 'all_bijou'
    def get_queryset(self):
        return bijou.objects.all()

def ContactUs(request):
    return render(request,'store/contact.html')

class DetailView(generic.DetailView):
    model = bijou
    slug_url_kwarg = 'name'
    slug_field = 'name'
    template_name = 'store/detail.html'

class BijouCreat(CreateView):
    model = bijou
    fields = ['name','color','price','image_link']
    template_name = 'store/bijou_form.html'

class BijouDelete(DeleteView):
    model = bijou
    slug_field = 'name'
    success_url = reverse_lazy('store:store_page')