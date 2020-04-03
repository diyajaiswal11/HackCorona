from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import PassForm
from django.utils import timezone
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import PassModel


# Create your views here.
def home(request):
    return render(request,'home.html')


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

def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None


class ViewPDF(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('pdf.html')
		return HttpResponse(pdf, content_type='application/pdf')


class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('pdf.html')
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "LockdownPass.pdf"
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response



def index(request,uniquenumber):
    if PassModel.objects.filter(uniquenumber=uniquenumber).exists():
        context={}
        return render(request, 'pdf_template.html', context=context)
