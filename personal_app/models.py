from django.db import models

# Create your models here.
class Interests(models.Model):
    name = models.CharField(max_length=50)
    icon = models.CharField(max_length = 150)
    color = models.CharField(max_length = 150)
    
    def __str__(self):
        return self.name
    
class Services(models.Model):
    title = models.CharField(max_length = 150)
    icon = models.CharField(max_length = 150)
    description = models.TextField()
               
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    subject = models.CharField(max_length = 150)
    message = models.TextField()
        
    class Meta:    
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.email