from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import StudentData, AdminData
from django.contrib import messages

# Create your views here.

# adding he admin login page logic 
def admin_login(request):
    return render(request, 'admin_login.html')




# adding the student login page logic 
def student_login(request):
    return render(request, 'student_login.html')



#  adding the signup page logic 
def signup(request):
    if request.method == "POST":
        role = request.POST.get('role')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        userId = request.POST.get('userId')
        department = request.POST.get('department')
        password = request.POST.get('password')

        if role == 'student':
            if StudentData.objects.filter(email=email).exists() or StudentData.objects.filter(student_id=userId).exists():
                messages.error(request, "⚠️ Email is already in use!")
                return redirect("/signup/")
        
            StudentData.objects.create(
                fname = fname,
                lname = lname,
                email = email,
                student_id = userId,
                department = department,
                password = password
            )
            messages.success(request, "✅ Student registered successfully!")
            return redirect("/student_login/")

        elif role == 'admin':
            if AdminData.objects.filter(email=email).exists() or AdminData.objects.filter(admin_id=userId).exists():
                messages.error(request, "⚠️ Email already in use!")
                return redirect("/signup/")
            
            AdminData.objects.create(
                fname = fname,
                lname = lname,
                email = email,
                admin_id = userId,
                password = password
            )
            messages.success(request, "✅ Admin registered successfully!")
            return redirect('/admin_login/')
        
    

    return render(request, 'signup.html')