from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . models import CBCresults, WBCdifferential
from .forms                         import CBCform
import pandas as pd

# Create your views here.

class CBCListView(ListView):
    model = CBCresults
    date = CBCresults.objects.all().order_by('date')
    template_name = "CBCdatatable.html"

def CBCGraphView(request):
    model = CBCresults
    date = CBCresults.objects.values_list('date', flat = True).order_by('date')
    WBC = CBCresults.objects.values_list('WBC', flat = True)
    RBC = CBCresults.objects.values_list('RBCs', flat = True)
    NRBC = CBCresults.objects.values_list('NRBC', flat = True)
    return render(request, 'CBCgraphs.html', 
        {'date': date, 'WBC':WBC, 'RBC':RBC, 'NRBC':NRBC})


class CBCCreateView(CreateView):
    model = CBCresults
    template_name = 'cbc_new.html'
    fields = '__all__'

class CBCUpdateView(UpdateView):
    model = CBCresults
    fields = '__all__'
    template_name = 'cbc_edit.html'

class BlogDeleteView(DeleteView):
    model = CBCresults
    template_name = 'cbc_delete.html'
    success_url = reverse_lazy('home')

class WBCDifferentialCreateView(CreateView):
    model = WBCdifferential
    template_name = 'wbc_diff_new.html'
    fields = '__all__'




# def CBCCreateView(request):
#     form = CBCform(request.POST)
    
#     if request.method == 'POST':
#         form = CBCform(request.POST)
#         if form.is_valid():
#             temp = form.save(commit=False)
#             #profile.applyFor = form.cleaned_data.get('applyFor') ###
#             #profile.orgTheme = form.cleaned_data.get('orgTheme') ###
#             #profile.save()
#             temp.save()
#             return redirect(reverse('cbcresultslist', kwargs={"pk": temp.pk}))
#     else:
#         form = CBCform()

#     CBC=CBCresults.objects.all()
    
#     return render(request, 'cbc_new.html', {'form': form,'CBC':CBC})
    
