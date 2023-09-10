from django.db import models


class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'api_tasks'
