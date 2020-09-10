from django.shortcuts import render
from .conversationStarters import randomQuestion

# Create your views here.

def index(request):
    return render(request, "home/index.html")

def deep(request):
    return render(request, "home/deep.html")

def fun(request):
    if request.method == "POST":

        print("post")

        questions = []
        for x in range(3):
            questions.append(randomQuestion())

        return render(request, "home/fun.html", {
            "questions": questions
        })
    else:
        print("get")
        return render(request, "home/fun.html")