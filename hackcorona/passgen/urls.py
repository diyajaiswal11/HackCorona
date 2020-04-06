from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('fillform/',views.fillform,name='fillform'),
    path('download/',views.download,name='download'),
    path('epass/<uniquenumber>/', views.index,name='epass'),
    path('pdf_view/<uniquenumber>/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/<uniquenumber>/', views.DownloadPDF.as_view(), name="pdf_download"),
    path('precautions/',views.precautions,name='precautions'),
    path('faq/',views.faqpage,name='faqpage'),
    path('helpline/pdf/',views.helpline,name='helpline')
]
