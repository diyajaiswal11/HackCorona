from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('fillform/',views.fillform,name='fillform'),
    path('epass/<uniquenumber>/', views.index,name='epass'),
    path('pdf_view/<uniquenumber>/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/<uniquenumber>/', views.DownloadPDF.as_view(), name="pdf_download"),
    path('faq/',views.faqpage,name='faqpage'),
    path('precautions/',views.precautions,name='precautions'),
]
