from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views
from .views import CBCCreateView


urlpatterns = [
    url(r'^about/', TemplateView.as_view(template_name="about.html"), name = 'about'),
    path('', TemplateView.as_view(template_name="home.html"), name = 'home'),
    path('results/reviewcbcresults', views.CBCListView.as_view(), name = 'cbcresultslist'),
    path('manage/mywbcresults', views.CBCGraphView, name = 'cbcresultsgraphs'),
    path('add/cbc/', views.CBCCreateView.as_view(), name = 'cbc_new'),
    path('add/wbc/', views.WBCDifferentialCreateView.as_view(), name = 'wbcdiff'),
    path('edit/<int:pk>/cbc/',views.CBCUpdateView.as_view(), name='cbc_edit'),
    path('post/<int:pk>/delete/',views.BlogDeleteView.as_view(), name='cbc_delete'),
]