from django.db import models

class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"'{self.title}' by {self.author}"
