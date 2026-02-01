from django.shortcuts import render,redirect
from home.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')


@login_required(login_url='login_page')
def services(request):
    queryset = NewService.objects.all().values()
    context = {'queryset':queryset}
    return render(request, 'services.html',context)
def careers(request):
    return render(request, 'careers.html')
def about_us(request):
    return render(request, 'about_us.html')
def apply_page(request,id):
    if request.method == 'POST':
       name =request.POST.get('name')
       age =request.POST.get('age')
       gender =request.POST.get('gender')           
       email =request.POST.get('email')
       mobile =request.POST.get('mobile')
       messages.success(request, "Your application has been submitted successfully!")
       s1 =Applicant.objects.create(name = name,age =age,mobile=mobile,gender=gender,email_add= email)
       s1.save()
       return redirect('services')

    return render(request, 'apply_page.html')




def login_page(request):
    if request.method == 'POST':
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username,password)
    
        if not User.objects.filter(username = username).exists():
            messages.error(request, "Username not exist")
            return redirect('login_page')
        else:
           x = authenticate(request,username=username,password=password)
           if x is None:
              
              messages.error(request,"invalid credentials")
              return redirect('login_page')
           else:
               messages.success(request,"log in success!")
               login(request,user = x)
               return redirect('/')
            
        # print(username,password)
    return render(request,'login.html')
        
def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username = username).exists():
            messages.error(request, "Username Already Taken")
        else:
            user = User.objects.create(first_name = first_name, last_name = last_name, email = email, username = username)

            user.set_password(password)

            user.save()
            messages.success(request, "Account Created Successfully")
            return redirect('login_page')

            
    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect('/')


def submit_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        # Save data to the database
        CandidateDetails.objects.create(name=name, email=email, phone=phone)
        return HttpResponse("Thank you for registering. We will notify you of future updates.")
    return redirect('careers')



def careers(request):
    search_query = request.GET.get('search', '')
    if search_query:
        jobs = Job.objects.filter(title__icontains=search_query)  # Search functionality
    else:
        jobs = Job.objects.all()  # Fetch all jobs
    return render(request, 'careers.html', {'jobs': jobs})

def culture(request):
    return render(request, 'culture.html')

def education(request):
    return render(request, 'education.html')

def historical_place(request):
    return render(request, 'historical_place.html')

def facilities(request):
    return render(request, 'facilities.html')