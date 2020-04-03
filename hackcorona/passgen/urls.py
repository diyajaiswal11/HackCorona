from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('fillform/',views.fillform,name='fillform'),
    path('epass/<uniquenumber>/', views.index,name='epass'),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
]