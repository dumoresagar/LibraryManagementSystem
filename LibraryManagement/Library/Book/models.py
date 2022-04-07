from django.db import models

# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=100)
    author=models.CharField(max_length=40)
    category=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name},{self.author},{self.category}"

class Student(models.Model):
    book = models.OneToOneField(Book,on_delete=models.CASCADE)
    full_name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    date_of_issue = models.DateTimeField()

    def __str__(self):
        return f"{self.book},{self.full_name},{self.address},{self.date_of_issue}"


