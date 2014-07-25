from django.conf.urls import patterns, url


from whimsy import views

urlpatterns = patterns('',
#    url(r'^(?P<letter_id>\d+)/$', views.letter, name = 'letter'),
    url(r'^markov/$', views.markov_sentence, name = 'markov'),
    url(r'^random/$', views.random_sentence, name = 'random'),

)

