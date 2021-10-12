from django.db import models

class ClassType(models.IntegerChoices):
    ASHTANGA = 1, 'Ashtanga'
    BARRE = 2, 'Barre'
    MEDITATION = 3, 'Meditation'
    PILATES = 4, 'Pilates'
    TAI_CHI = 5, 'Tai Chi'
    VINYASA =  6, 'Vinyasa'