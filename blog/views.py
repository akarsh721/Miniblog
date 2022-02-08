from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import signupAuthor, Postfm
from .models import AuthorRegister, Post
from django.contrib import messages
from django.contrib.auth import authenticate, logout


# Create your views here.

def home(request):
    posts = Post.objects.all()
    if posts:
        return render(request,'blog/home.html',{'posts':posts})
    else:
        return render(request,'blog/home.html')

def dashbaord(request):
    loggedinUser = request.session.get('user')
    # loggedinUserObj = AuthorRegister.objects.get(username = loggedinUser)
    loggedinUserPosts = Post.objects.filter(author = loggedinUser)
    # print(loggedinUserPosts)
    return render(request,'blog/dashboard.html',{'posts':loggedinUserPosts,'user':loggedinUser})

def about(request):
    return render(request,'blog/about.html')

def contact(request):
    return render(request,'blog/contact.html')


def userlogin(request):
        if request.method == 'POST':
            uname = request.POST['username']
            upass = request.POST['password']

            loginCheck = AuthorRegister.objects.filter(username = uname, password1 = upass)
            if loginCheck:
                print("Logged In successfully")
                request.session['user'] = uname
                messages.add_message(request,messages.SUCCESS,'Logged In successfully')
                return redirect("/dashboard/")
            else:
                messages.add_message(request,messages.ERROR,'Invalid Username or password')
                print("Invalid credentials")
        else:
            print("something went wrong")
        return render(request,'blog/login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            fm = signupAuthor(request.POST)
            if fm.is_valid():
                fm.save()
                messages.add_message(request,messages.SUCCESS,"Successfully Registered!")
                return redirect("/")
            else:
                print(fm.errors)
                messages.add_message(request,messages.ERROR,fm.errors)
        else:
            print("pswd did not match")
            messages.add_message(request,messages.ERROR,"Password did not match! Try again")
    else:
        fm = signupAuthor()
    return render(request,'blog/signup.html')

def userlogout(request):
    logout(request)
    return HttpResponseRedirect("/")


def createPost(request):
    loggedinUser = request.session.get('user')
    if loggedinUser:
        # Not needed obj for other details here as only username is required
        # loggedinUserObj = AuthorRegister.objects.get(username = loggedinUser)
        if request.method == 'POST':
            newpost = Postfm(request.POST)
            if newpost.is_valid():
                newpost.save()
                messages.add_message(request,messages.SUCCESS,'Posted Successfully')
            else:
                print(newpost.errors)
        else:
            newpost = Postfm()
        return render(request,'blog/newpost.html',{'username':loggedinUser})
    else:
        return render(request,'blog/newpost.html')

def updatepost(request,id):
    postObj = Post.objects.get(pk = id)
    if request.method == 'POST':
        updatepost = Postfm(request.POST,instance=postObj)
        if updatepost.is_valid():
            updatepost.save()
            print("Post updated successfully")
            return redirect('/dashboard/')
        else:
            print(updatepost.errors)
            messages.add_message(request,messages.ERROR,updatepost.errors)
    
    else:
        updatepost = Postfm()
    return render(request,'blog/updatepost.html',{'posts':postObj})

def deletepost(request,id):
    postObj = Post.objects.get(pk = id)
    postObj.delete()
    return redirect("/dashboard/")


def adminlogin(request):
    if request.method == 'POST':
        uname = request.POST["username"]
        upass = request.POST["password"]

        if uname == 'admin' and upass == 'admin123':
            # messages.add_message(request,messages.SUCCESS,"Logged in successfully")
            print("LoggedIn successfully")
            return redirect("/adminpanel/")
            #Admin Page
        else:
            print("Invalid credentials")
            messages.add_message(request,messages.ERROR,"Invalid Credentials, Try Again")

    return render(request,'blog/adminlogin.html')


def adminpanel(request):
    authordata = AuthorRegister.objects.all()
    return render(request,'blog/adminpage.html',{'authordata':authordata})

def showpost(request,id):
    postObj = Post.objects.filter(pk = id)
    return redirect(request,"blog/showpost.html",{'authorposts' : postObj})

def adminRemoveAuthor(request,id):
    authorObj = AuthorRegister.objects.get(pk = id)
    authorObj.delete()
    return HttpResponseRedirect("/adminpanel/")

