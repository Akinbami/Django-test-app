from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields=['full_name','email','matric_no']



    def clean_email(self):
        '''
        This function validates the email field in the form
        '''
        email=self.cleaned_data.get('email')
        email_base, provider= email.split('@')
        domain, extension=provider.split('.')
        if not domain=='gmail':
            raise forms.ValidationError("please enter a valid .gmail email. address")
        if not extension == 'edu':
            raise forms.ValidationError("please enter a valid email address with the correct .edu extenstion")
        return email

   
