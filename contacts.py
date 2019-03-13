from django.db import models
import uuid
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=250)
    created = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    support_email = models.EmailField(max_length=250)
    order_email = models.EmailField(max_length=250)
    def __str__(self):
        return self.name

class SupportRequest(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(default=uuid.uuid4,editable=False)

    def get_absolute_url(self):
        return reverse('website:support-detail', kwargs={'uuid': self.uuid})

    def __str__(self):
        return self.email


class NewModel(models.Model):
    field_one = models.CharField(max_length=50)
    field_two = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
