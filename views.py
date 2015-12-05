from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from whimsy.models import Sentence
# Create your views here.

def test(request):
    context = {
    'request' : request, 
    }
    return render(request, 'whimsy/test.html', context)

#quasi api thing

def markov_sentence(request):
    s = Sentence()
    return HttpResponse(s.get_markov_sentence())

def random_sentence(request):
    s = Sentence()
    return HttpResponse(s.get_random_sentence())

def post_sentence(request, data, user):
    #TODO: figure out clickjacking protection
    print data
    s = Sentence()
    u = User.objects.get(id = user)
    print u
    return s.post_sentence(data, u)
