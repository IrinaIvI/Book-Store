from django.db import models

class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    count = models.IntegerField(default=0)
