from django.db import models

from django.utils.encoding import python_2_unicode_compatible


# Register your models here.
@python_2_unicode_compatible
class userlogin(models.Model):
    username = models.CharField(u'username', max_length=20)
    password = models.CharField(u'password', max_length=45)

    def __str__(self):
        return self.username

