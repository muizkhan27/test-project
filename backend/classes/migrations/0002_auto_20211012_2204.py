# Generated by Django 3.2.8 on 2021-10-12 22:04

from django.db import migrations
import random

def forwards_func(apps, schema_editor):
    OnlineClass = apps.get_model("classes", "OnlineClass")
    Teacher = apps.get_model("teachers", "Teacher")
    db_alias = schema_editor.connection.alias

    VINNY = Teacher.objects.using(db_alias).filter(name='Vinny Yasa').first()
    ASHLEY = Teacher.objects.using(db_alias).filter(name='Ashley Tanga').first()
    ANNE = Teacher.objects.using(db_alias).filter(name='Anne Usara').first()
    VICK = Teacher.objects.using(db_alias).filter(name='Vick Rum').first()
    MINDY = Teacher.objects.using(db_alias).filter(name='Mindy Fuller').first()

    ASHTANGA = 1
    BARRE = 2
    MEDITATION = 3
    PILATES = 4
    TAI_CHI = 5
    VINYASA =  6

    classes_to_add = []
    for m in range(1,13):
        classes_to_add.append(OnlineClass(
            name='Vinyasa with Vinny {m}'.format(m=m), 
            type=VINYASA,
            start='2021-{m:02d}-11T11:00:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=VINNY,
        ))
        classes_to_add.append(OnlineClass(
            name='Meditation with Vinny {m}'.format(m=m), 
            type=MEDITATION,
            start='2021-{m:02d}-02T09:30:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=VINNY,
        ))
        classes_to_add.append(OnlineClass(
            name='Ashtanga with Vinny {m}'.format(m=m), 
            type=ASHTANGA,
            start='2021-{m:02d}-25T12:30:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=VINNY,
        ))
        classes_to_add.append(OnlineClass(
            name='Ashtanga with Ashley {m}'.format(m=m), 
            type=ASHTANGA,
            start='2021-{m:02d}-22T14:00:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=ASHLEY,
        ))
        classes_to_add.append(OnlineClass(
            name='Meditation with Ashley {m}'.format(m=m), 
            type=MEDITATION,
            start='2021-{m:02d}-08T18:00:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=ASHLEY,
        ))
        classes_to_add.append(OnlineClass(
            name='Barre with Anne {m}'.format(m=m), 
            type=BARRE,
            start='2021-{m:02d}-05T17:00:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=ANNE,
        ))
        classes_to_add.append(OnlineClass(
            name='Pilates with Anne {m}'.format(m=m), 
            type=PILATES,
            start='2021-{m:02d}-14T10:30:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=ANNE,
        ))
        classes_to_add.append(OnlineClass(
            name='Tai Chi with Anne {m}'.format(m=m), 
            type=TAI_CHI,
            start='2021-{m:02d}-19T06:30:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=ANNE,
        ))
        classes_to_add.append(OnlineClass(
            name='Tai Chi with Vick {m}'.format(m=m), 
            type=TAI_CHI,
            start='2021-{m:02d}-20T07:30:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=VICK,
        ))
        classes_to_add.append(OnlineClass(
            name='Vinyasa with Vick {m}'.format(m=m), 
            type=VINYASA,
            start='2021-{m:02d}-21T13:30:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=VICK,
        ))
        classes_to_add.append(OnlineClass(
            name='Barre with Vick {m}'.format(m=m), 
            type=BARRE,
            start='2021-{m:02d}-05T12:00:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=VICK,
        ))
        classes_to_add.append(OnlineClass(
            name='Meditation with Vick {m}'.format(m=m), 
            type=MEDITATION,
            start='2021-{m:02d}-16T09:15:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=VICK,
        ))
        classes_to_add.append(OnlineClass(
            name='Meditation with Mindy {m}'.format(m=m), 
            type=MEDITATION,
            start='2021-{m:02d}-05T11:30:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=MINDY,
        ))
        classes_to_add.append(OnlineClass(
            name='Pilates with Mindy {m}'.format(m=m), 
            type=PILATES,
            start='2021-{m:02d}-19T12:30:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=MINDY,
        ))
        classes_to_add.append(OnlineClass(
            name='Ashtanga with Mindy {m}'.format(m=m), 
            type=ASHTANGA,
            start='2021-{m:02d}-26T15:00:00.000Z'.format(m=m),
            duration=random.randrange(15, 90, 5),
            teacher=MINDY,
        ))

    OnlineClass.objects.using(db_alias).bulk_create(classes_to_add)

def reverse_func(apps, schema_editor):
    OnlineClass = apps.get_model("classes", "OnlineClass")
    db_alias = schema_editor.connection.alias
    OnlineClass.objects.using(db_alias).all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]