from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # ... other fields

    def __str__(self):
        return self.title
