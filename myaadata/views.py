from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins     import LoginRequiredMixin

from . models import CBCresults, WBCdifferential
from .forms                         import CBCform

# Create your views here.

class CBCListView(LoginRequiredMixin, ListView):
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

class CBCCreateView(LoginRequiredMixin, CreateView):
    model = CBCresults
    template_name = 'cbc_new.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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
