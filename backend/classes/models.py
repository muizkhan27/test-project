from django.db import models
from .enums import ClassType
from teachers.models import Teacher

class OnlineClass(models.Model):
    name = models.CharField('Name', max_length=255)
    type = models.IntegerField(
        'Class instruction type',
        choices=ClassType.choices,
        default=ClassType.MEDITATION
    )
    start = models.DateTimeField('Start')
    duration = models.IntegerField('Duration (minutes)')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, primary_key=False)

    def __str__(self):
        return '{name} on {date} ({id})'.format(
            name=self.name,
            date=self.start.strftime('%m/%d @ %H:%M'),
            id=self.pk
        )
