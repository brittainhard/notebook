from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, default="", unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=255, default="")
    text = models.TextField(default="")
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
