from django.db import models
from django.contrib.auth.models import User, AnonymousUser
import random, re



# Create your models here.

class Sentence(models.Model):
    sentence = models.CharField(max_length = 300, blank = False)
    submitter = models.ForeignKey(User)

    def __unicode__(self):
        return self.sentence

    #returns a random sentence from the database
    def get_random_sentence(self):
        #TODO write actual randomization
        #this method is hyper-inefficient for large DBs
        return Sentence.objects.order_by('?')[0].sentence

    #the meat of this app, returns a generated sentence terminated by a period
    def get_markov_sentence(self):
        #TODO actually write this, lol

        
        output = 'butts, lol'
        return output

    def post_sentence(self, data, user):
        if data == '' or len(data) > 299:
            return False
        else:
            if re.search(r'[?!.]', data) == None:
                data = data + '.'
            self.sentence = data
            try:
                self.submitter = user
            except:
                return False
            self.save()
            return True
