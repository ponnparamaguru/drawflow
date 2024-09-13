from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='node_images/', blank=True, null=True)
    no_of_inputs = models.IntegerField()
    no_of_outputs = models.IntegerField()

    def __str__(self):
        return self.name

class Flow(models.Model):
    name = models.CharField(max_length=255)
    data = models.JSONField()  # Or use TextField if you need a large string

    def __str__(self):
        return self.name
