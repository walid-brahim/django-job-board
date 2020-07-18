from django.db import models

# Create your models here.

def uploadimage(instance , filename):
    imagename , extension = filename.split(".")
    return "photo/%s.%s"%(instance.id , extension)

class job(models.Model) : 

     
     title = models.CharField(max_length = 50)
     description = models.TextField(max_length = 300)
     Published_at = models.DateTimeField(auto_now= True)
     Vacancy = models.IntegerField(default= 0)
     Salary = models.IntegerField(default= 0)
     image = models.ImageField(upload_to=uploadimage)

     def __str__ (self):
         return self.title