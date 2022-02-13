from django.shortcuts import render
from django.http import HttpResponse

#
from outline import forms
from outline.models import Person,Publication,Plate,Depiction,Retouch_Depiction,Retouch,Metrics,R_Import,Artefact,UserProfileInfo

#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Created views

def index (request):
    #ID = {'insert_ID':'!'}
    plate_list = Plate.objects.order_by('page')
    plate_dict = {'plate' : plate_list,'text':'hello world','number':10}

    return render(request,'outline/index.html',context = plate_dict)

@login_required
def special(request):
    return render (request,'outline/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('outline:index'))


# Add Author
def form_person(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #Do something code

            print ('validation success!')
            print (form.cleaned_data['firstname'])
            print (form.cleaned_data['surname'])
            print (form.cleaned_data['affiliation'])
            print (form.cleaned_data['email'])

    return render(request,'outline/form_person.html',{'form' :form})

# Add Publication
def form_publication (request):
    form = forms.Publication_Form()

    if request.method == 'POST':
        form = forms.Publication_Form(request.POST)

        if form.is_valid():
            #Do something code
            form.save()
            print ('validation success!')
            print (form.cleaned_data)

    return render(request,'outline/form_publication.html',{'form' :form})

def registration (request):
    registered = False

    if request.method == 'POST':

        user_form = forms.UserForm (data = request.POST)
        profile_form = forms.UserProfileInfoForm (data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            #Do something code
            user = user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            register = True

            #return index(request)
        else:
            raise ValueError('Registration failed!')

    else:

        user_form = forms.UserForm ()
        profile_form = forms.UserProfileInfoForm ()

    return render(request,'outline/form_registration.html',
        {'user_form':user_form,
         'profile_form':profile_form,
         'registered':registered})

def user_login (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('outline:index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print('Someone failed logging in')
            print('username:{} and password:{}'.format(username,password))
            return HttpResponse('invalid login details supplied!')
    else:
        return render(request,'outline/login.html',{})

def form_person(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #Do something code

            print ('validation success!')
            print (form.cleaned_data['firstname'])
            print (form.cleaned_data['surname'])
            print (form.cleaned_data['affiliation'])
            print (form.cleaned_data['email'])

    return render(request,'outline/form_person.html',{'form' :form})



def import_tools (request):
    ID = {'insert_ID':'tools!'}
    return render(request,'outline/retouch.html',context =ID)


def retouch (request):
    ID = {'insert_ID':'retouch!'}
    return render(request,'outline/retouch.html',context =ID)
