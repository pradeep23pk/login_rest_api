from django.db import models
import random, string

def pass_key():
    key = ''.join(random.choice(string.ascii_letters) for i in range(8))
    return key

class user(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField()
    passwords = models.CharField(max_length=100)
    referral_code=models.CharField(max_length=100,default=pass_key)
    incentives=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class RefCode(models.Model):
    code=models.CharField(max_length=10)
    from_name=models.CharField(max_length=100, verbose_name="")
    to_name=models.CharField(max_length=100)

    def __str__(self):
        return self.code


class history(models.Model):
    usingCode=models.CharField(max_length=10)
    userEmail=models.EmailField()
    userIncentive=models.IntegerField(default=0)
    referalEmail=models.EmailField()
    referalIncentive=models.IntegerField(default=0)


    def __str__(self):
        return self.usingCode
