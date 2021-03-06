from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.

def index(request):
    if request.session.get('words') == None:
        request.session['words'] = []
    return render(request, 'sessionwords/index.html')

def add_word(request):
    word = request.POST['word']
    color = request.POST['color']
    if "font_size" in request.POST:
        font = "big"
    else:
        font = "normal"
    created_at = datetime.strftime(datetime.now(), "&H:%M:%S %p, %B %d, %Y")

    request.session['words'].append({'word': word, 'color': color, 'font': font, 'created_at': created_at})
    request.session.modified = True
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')