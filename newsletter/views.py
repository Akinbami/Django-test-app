from django.shortcuts import render
from .form import SignUpForm
# Create your views here.
def home(request):
    title='My Title {0}'.format(request.user)
    if request.method=='POST':
        print request.POST
    form=SignUpForm(request.POST or None)
    
    context={
        "template_title":title,
        "form":form,
    }
    
    if form.is_valid():
        instance = form.save(commit=False)
        print instance.email
        print instance.matric_no
        instance.save()
        
        context={
            "title":"Thank You",
        }
    return render(request,'home.html',context)
