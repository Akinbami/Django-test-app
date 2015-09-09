from django.contrib import admin

# Register your models here.
from .form import SignUpForm
from .models import SignUp
class SignUpAdmin(admin.ModelAdmin):
    list_display=['__unicode__', 'full_name','email', 'datetime', 'update']
    form=SignUpForm
    #class Meta:
    #    model=SignUp

admin.site.register(SignUp, SignUpAdmin)
