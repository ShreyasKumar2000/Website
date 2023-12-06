from django.db import models

# Create your models here.
class project(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='image')
    cost=models.FloatField()
    project_desc=models.TextField()

    def __str__(self):
        return self.name