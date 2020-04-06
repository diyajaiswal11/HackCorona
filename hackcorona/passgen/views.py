from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import PassForm,DownloadForm
from django.utils import timezone
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import PassModel
from django.contrib.auth.models import auth 
from django.utils.translation import template

# Create your views here.
def home(request):
    return render(request,'home.html')

def faqpage(request):
    return render(request,'faq.html')

def precautions(request):
    return render(request,'precautions.html')

def helpline(request):
    return render(request,'helpline.html')

def fillform(request):
    if request.method=="POST":
        form=PassForm(request.POST,request.FILES) 
        if form.is_valid():
            p=form.save()
            p.issuedate=timezone.now()
            p.uniquenumber=str(p.uniquenumber)+str(p.id)
            p.save()
            return HttpResponseRedirect(reverse('epass',args=[p.uniquenumber]))
    else:
        form=PassForm()
    context={'form':form }
    return render(request,'fillform.html',context)

def download(request):
    if request.method=="POST":
        form=DownloadForm(request.POST)
        if form.is_valid():
            number=form.cleaned_data['aadharcardnumber']
            if PassModel.objects.filter(aadharcardnumber=number).exists():
                user=PassModel.objects.get(aadharcardnumber=number)
                return HttpResponseRedirect(reverse('epass',args=[user.uniquenumber]))
            else:
                return redirect('download')
    else:
        form=DownloadForm()
    context={'form':form}
    return render(request,'download.html',context)


def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


class ViewPDF(View):
    def get(self, request,uniquenumber,*args, **kwargs):
        try:
            if PassModel.objects.filter(uniquenumber=uniquenumber).exists():
                context={
                    'a': PassModel.objects.get(uniquenumber=uniquenumber),
                }
                pdf =render_to_pdf('pdf.html',context)
                return HttpResponse(pdf,content_type='application/pdf')
        except PassModel.DoesNotExist:
            return redirect('fillform')

class DownloadPDF(View):
    def get(self,request,uniquenumber,*args, **kwargs):
        try:
            if PassModel.objects.filter(uniquenumber=uniquenumber).exists():
                context={
                    'a':PassModel.objects.get(uniquenumber=uniquenumber),
                }
                pdf=render_to_pdf('pdf.html',context)
                response=HttpResponse(pdf,content_type='application/pdf')
                filename = "LockdownPass.pdf"
                content = "attachment; filename='%s'" %(filename)
                response['Content-Disposition'] = content
                return response
        except PassModel.DoesNotExist:
            return redirect('fillform')

def index(request,uniquenumber):
    try:
        if PassModel.objects.filter(uniquenumber=uniquenumber).exists:
            context={
                'a':PassModel.objects.get(uniquenumber=uniquenumber)    
            }
            return render(request,'pdf_template.html',context=context)
    except PassModel.DoesNotExist:
        return redirect('fillform')

