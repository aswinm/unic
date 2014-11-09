from django.db import models

class Enquiry(models.Model):

    def __unicode__(self):
        return self.name
    eid = models.AutoField(primary_key = True)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    desc = models.TextField(max_length=1000)

# Create your models here.
