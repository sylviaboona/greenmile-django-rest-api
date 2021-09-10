from django.db import models

# Create your models here.
class Loader(models.Model):
    registration_date = models.DateTimeField('registration date', auto_now=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.full_name}'

class Supplier(models.Model):
    registration_date = models.DateTimeField('registration date', auto_now=True)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    phone = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200, default='company-name')
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.company_name}'


class Package(models.Model):
    date_added = models.DateTimeField('date added', auto_now=True)
    package_name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    receipient = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, default='company-name')
    def __str__(self):
        return f'{self.company_name}'
