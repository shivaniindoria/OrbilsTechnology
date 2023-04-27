from django.db import models

# Create your models here.
class Contact(models.Model):
    # msg_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.CharField(max_length=30, default="")
    number = models.IntegerField(default="0")
    querry = models.CharField(max_length=1000, default="")
    add1 = models.CharField(max_length=60, default="")
    add2 = models.CharField(max_length=60, default="")
    country = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=20, default="")
    zip = models.IntegerField(default="0")

#change name of product in db list
    def __str__(self):
        return self.firstname

class Courses(models.Model):
    courseimg = models.ImageField(upload_to="courses")
    coursename = models.CharField(max_length=20,default="")
    subheading = models.CharField(max_length = 20,default="")
    courseId = models.CharField(max_length=10,default="")
    shortdescription = models.CharField(max_length=80,default="")
    description = models.CharField(max_length=300,default="")
    courseduration = models.CharField(max_length=20,default="")
    def __str__(self):
        return self.coursename

# class Events(models.Model):
#     event_headline = models.CharField(max_length=120)
#     heading = 
#     description = 
#     date = 
#     venue = 
#     reg_deadline = 
#     image1 = 
#     image1 = 
#     image1 = 
#     other = 
#     guests = 
#     guest_image =
#     guests_description = 
