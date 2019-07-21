from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='com', null=True)
    author = models.CharField(max_length=10)
    message = models.TextField()