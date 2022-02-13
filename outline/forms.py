from django import forms
from django.contrib.auth.models import User
from django.core import validators

from outline.models import Person,Publication,Plate,Depiction,Retouch_Depiction,Retouch,Metrics,R_Import,Artefact,UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields =('username','email','password')

class UserProfileInfoForm (forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('affiliation','profile_pic')


class FormName(forms.Form):
    firstname = forms.CharField(required = True)#, validators=[check_for_z])
    surname = forms.CharField(required = True)
    affiliation = forms.CharField(required = True)
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')

    def clean(self):
        all_clean_data = super().clean()

        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Make sure emails match!')

class Publication_Form (forms.ModelForm):

    # Form fields go here
    class Meta:
        model = Publication
        fields =  '__all__' #  '__all__'

# class NewUser_Form (forms.ModelForm):
#
#     # Form fields go here
#     class Meta:
#         model = Registration
#         fields =  '__all__' #  '__all__'



    # botcatcher = forms.CharField(required = False,
    #                 widget=forms.HiddenInput,
    #                 validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #
    #     if len (botcatcher)>0:
    #         raise forms.ValidationError('Gottcha Bot!')
    #
    #     return botcatcher
