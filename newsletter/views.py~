from django.shortcuts import render
from .form import SignUpForm
# Create your views here.
class view(SignUpForm):
    def home(request):
        title='My Title {0}'.format(request.user)
        form=SignUpForm()
        context={
            "template_title":title,
            "form":form,
         }
        return render(request,'home.html',context)
