from django.db import models

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=30)

    # class Meta:
    #     ordering=['post']

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.FileField(blank=True)
    tag = models.ManyToManyField(Tag)

    # def __str__(self):
    #     return self.name.name


    