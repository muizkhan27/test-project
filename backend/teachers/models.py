from django.db import models

class Teacher(models.Model):
    name = models.CharField('Name', max_length=255)

    def __str__(self):
        return '{name} ({id})'.format(
            name=self.name,
            id=self.pk
        )

