from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import customUserModel
from django.contrib.auth import get_user_model 
from allauth.account.forms  import LoginForm, SignupForm 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Button, Fieldset, Field, Div, HTML
from crispy_forms.bootstrap import StrictButton

class customUserCreationForm(UserCreationForm):

    class meta:
        model = get_user_model()
        fields = ('email, username', )


class customUserChangeForm(UserChangeForm):

    class meta:
        model = get_user_model()
        fields = ('email, username', )


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields.keys():
            if fieldname == 'login':
                self.fields['login'].widget.attrs.update({
                'class': 'form-label',
                'id': 'form2Example1'
                })
                self.fields['login'].label = ""
            elif fieldname == 'password':
                print(self.fields['password'].__dict__)
                print(self.fields['password'].label.__dict__)
               
                self.fields['password'].widget.attrs.update({
                    'class': 'form-label',
                    'id': 'form2Example2'
                })
                self.fields['password'].label = ""
        
        self.helper = FormHelper()
        print(Layout().__dict__)
        self.helper.layout = Layout(
            Field('login', css_id="form2Example1", css_class="mb-4" ), 
            Field('password', css_id="form2Example2", css_class="mb-4"),
            Div(
                StrictButton('login', type="submit", css_class="btn-success btn-rounded"), 
                css_class="d-flex justify-content-end pt-1 mb-4"
            )

        )


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in self.fields.keys():
            if fieldname == "username":
                self.fields['username'].widget.attrs.update({
                    'class': 'form-control',
                })
                self.fields['username'].label =''
            
            elif fieldname == 'email':
                self.fields['email'].widget.attrs.update({
                    'class': 'form-control'
                })
                self.fields['email'].label=''
            
            elif fieldname == 'password1':
                self.fields['password1'].widget.attrs.update({
                    'class' : 'form-control'
                })
                self.fields['password1'].label =''
            
            elif fieldname == 'password2':
                self.fields['password2'].widget.attrs.update({
                    'class' : 'form-control'
                })
                self.fields['password2'].label = ''
        
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('username', css_class='mb-4'),
            Field('email', css_class='mb-4'), 
            Field('password1', css_class='mb-4'),
            Field('password2', css_class='mb-4'),
            Div(
                StrictButton('Sign up', type='submit', css_class='btn btn-success btn-rounded'), 
                css_class='d-flex justify-content-end pt-1 mb-4')
        )



