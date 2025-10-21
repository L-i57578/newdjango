import time

from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render 
 
# Create your views here. 
def index(request): 
    return render(request, "singlepage/index.html") 
 
# The texts are much longer in reality, but have 
# been shortened here to save space 
texts = ["Text 1", "Text 2", "Text 3"] 
 
def section(request, num): 
    if 1 <= num <= 3: 
        return HttpResponse(texts[num - 1]) 
    else: 
        raise Http404("No such section")

def hello_world(request):
    return HttpResponse("Hello, World! 这是一个基础的Django应用。")

def single_page_app(request):
    return render(request, 'singlepage.html')

def scroll_page(request):
    return render(request, 'scroll.html')

def posts_index(request):
    return render(request, "posts/index.html")

def posts(request):
    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # Artificially delay speed of response
    time.sleep(1)

    # Return list of posts
    return JsonResponse({
        "posts": data
    })

def webpage(request):
    return render(request, "posts/webpage.html")

def animate(request):
    return render(request, "posts/animate.html")

def move(request):
    return render(request, "posts/move.html")

def react_app(request):
    return render(request, "posts/react-app.html")