from django.conf.urls import patterns, url


from whimsy import views

urlpatterns = patterns('',
    url(r'^test$', views.test, name = 'test'),
    url(r'^markov/$', views.markov_sentence, name = 'markov'),
    url(r'^random/$', views.random_sentence, name = 'random'),
    url(r'^post/(?P<data>.*)/(?P<user>.*)$', views.post_sentence, name = 'post'),
)

