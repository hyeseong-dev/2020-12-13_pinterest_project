from django.db import models

class HelloWorld(models.Model):
    text = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.text