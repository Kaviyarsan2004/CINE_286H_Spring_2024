from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Movie, record

def home(request):
    # Check is the user loging in
    movies = Movie.objects.all()[:6]
    movie1 = Movie.objects.get(pk=1)  # Assuming you have a movie with ID 1 in your database
    movie2 = Movie.objects.get(pk=2) 
    movie3 = Movie.objects.get(pk=3)  # Assuming you have a movie with ID 1 in your database
    movie4 = Movie.objects.get(pk=4) 
    movie5 = Movie.objects.get(pk=5)  # Assuming you have a movie with ID 1 in your database
    movie6 = Movie.objects.get(pk=6) 
    if request.method=='POST':
        username=request.POST['User_name']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successful!!")
            return redirect('home')
        else:
           messages.success(request,"ERROR: Try again or Register to Login!!")
           return redirect('home')
    else:
        return render(request,'home.html', {'movie1': movie1, 'movie2': movie2,  'movie3': movie3,  'movie4': movie4,  'movie5': movie5,  'movie6': movie6})

def User_logout(request):
     logout(request)
     messages.success(request,"Logout successful!!")
     return redirect('home')

def User_register(request):
    if request.method=='POST':
      form=SignUpForm(request.POST)
      if form.is_valid():
        form.save()
        #authenticate and login
        username =form.cleaned_data['username']
        password1=form.cleaned_data['password1']
        user=authenticate(username=username,password=password1)
        login(request,user)
        messages.success(request,'Successfully Registered!!')
        return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    template_name = f'movie_detail_{movie_id}.html'  # Example template name
    return render(request, template_name, {'movie': movie})



    
    




