from django.shortcuts import render
from .forms import PassForm
from django.utils import timezone
# Create your views here.
def home(request):
    return render(request,'home.html')


def fillform(request):
    if request.method=="POST":
        form=PassForm(request.POST,request.FILES) 
        if form.is_valid():
            p=form.save()
            p.issuedate=timezone.now()
            p.save()
            #return redirect('home') 
    else:
        form=PassForm() 
    context={'form':form }
    return render(request,'fillform.html',context)
