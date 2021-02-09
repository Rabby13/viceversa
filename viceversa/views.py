from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def reversed_text(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    words = len(user_text.split())
    return render(request, "reversed_text.html", {"user_text":user_text, "reversed_text":reversed_text, "words":words})