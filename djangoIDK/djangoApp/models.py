from django.db import models


class NoteModel(models.Model):
    name = models.CharField(max_length=51)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
