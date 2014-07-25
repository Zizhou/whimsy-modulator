from django.shortcuts import render
from django.http import HttpResponse

from whimsy.models import Sentence
# Create your views here.



#quasi api thing

def markov_sentence(request):
    s = Sentence()
    return HttpResponse(s.get_markov_sentence())

def random_sentence(request):
    s = Sentence()
    return HttpResponse(s.get_random_sentence())
