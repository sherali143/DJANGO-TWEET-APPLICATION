from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,redirect
from .models import Tweet
from django import forms
from .forms import TweetForm , UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'tweet.html')


def tweet_list(request):
    tweets= Tweet.objects.all().order_by('-created_at')
    names= User.objects.all()
    return render(request,'tweet_list.html', {'tweets':tweets,'names':names})


@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect ('tweet_list')      
    else:
        form = TweetForm()
    return render(request,'tweet_create.html',{'form':form})


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user= request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST,request.FILES,instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=request.user
            tweet.save()
            return redirect ('tweet_list')      
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_edit.html', {'form': form, 'tweet': tweet})


@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user= request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request,'tweet_delete.html', {'tweet':tweet})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tweet_list')  # Redirect to a page after successful registration
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

