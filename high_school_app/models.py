from django.db import models

# Create your models here.

class Stream(models.Model):
    stream_name = models.CharField(max_length=50)

    def __str__(self):
        return self.stream_name
    
class Student(models.Model):
    name = models.CharField(max_length=250)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def delete_student(self):
        self.delete()
