from django.db import models

# Create your models here.
class Interests(models.Model):
    name = models.CharField(max_length=150)
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
    
class Testmonials(models.Model):
    icon1 = models.CharField(max_length=150,blank=True,null=True)
    desc = models.TextField(blank=True,null=True)
    icon2 = models.CharField(max_length=150,blank=True,null=True)    
    profile = models.ImageField(upload_to='ProductImage',blank=True,null=True)
    nam = models.CharField(max_length = 150,blank=True,null=True)
    designation = models.CharField(max_length = 150,blank=True,null=True)
    
    def __str__(self):
        return self.nam
    
    
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