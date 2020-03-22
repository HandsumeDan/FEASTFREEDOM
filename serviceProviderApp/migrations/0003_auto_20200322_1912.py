# Generated by Django 3.0.4 on 2020-03-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceProviderApp', '0002_auto_20200322_1711'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kitchen2register',
            old_name='endTime',
            new_name='fridayEndTime',
        ),
        migrations.RenameField(
            model_name='kitchen2register',
            old_name='startTime',
            new_name='fridayStartTime',
        ),
        migrations.AddField(
            model_name='kitchen2register',
            name='mondayEndTime',
            field=models.CharField(choices=[('Tm1', '8:00'), ('Tm2', '8:30'), ('Tm3', '9:00'), ('Tm4', '9:30'), ('Tm5', '10:00'), ('Tm6', '10:30'), ('Tm7', '11:00'), ('Tm8', '11:30'), ('Tm9', '12:00'), ('Tm10', '12:30'), ('Tm11', '13:00'), ('Tm12', '13:30'), ('Tm13', '14:00'), ('Tm14', '14:30'), ('Tm15', '15:00'), ('Tm16', '15:30'), ('Tm17', '16:00'), ('Tm18', '16:30'), ('Tm19', '17:00')], default='Tm19', max_length=4),
        ),
        migrations.AddField(
            model_name='kitchen2register',
            name='mondayStartTime',
            field=models.CharField(choices=[('Tm1', '8:00'), ('Tm2', '8:30'), ('Tm3', '9:00'), ('Tm4', '9:30'), ('Tm5', '10:00'), ('Tm6', '10:30'), ('Tm7', '11:00'), ('Tm8', '11:30'), ('Tm9', '12:00'), ('Tm10', '12:30'), ('Tm11', '13:00'), ('Tm12', '13:30'), ('Tm13', '14:00'), ('Tm14', '14:30'), ('Tm15', '15:00'), ('Tm16', '15:30'), ('Tm17', '16:00'), ('Tm18', '16:30'), ('Tm19', '17:00')], default='Tm1', max_length=4),
        ),
        migrations.AddField(
            model_name='kitchen2register',
            name='saturdayEndTime',
            field=models.CharField(choices=[('Tm1', '8:00'), ('Tm2', '8:30'), ('Tm3', '9:00'), ('Tm4', '9:30'), ('Tm5', '10:00'), ('Tm6', '10:30'), ('Tm7', '11:00'), ('Tm8', '11:30'), ('Tm9', '12:00'), ('Tm10', '12:30'), ('Tm11', '13:00'), ('Tm12', '13:30'), ('Tm13', '14:00'), ('Tm14', '14:30'), ('Tm15', '15:00'), ('Tm16', '15:30'), ('Tm17', '16:00'), ('Tm18', '16:30'), ('Tm19', '17:00')], default='Tm19', max_length=4),
        ),
        migrations.AddField(
            model_name='kitchen2register',
            name='saturdayStartTime',
            field=models.CharField(choices=[('Tm1', '8:00'), ('Tm2', '8:30'), ('Tm3', '9:00'), ('Tm4', '9:30'), ('Tm5', '10:00'), ('Tm6', '10:30'), ('Tm7', '11:00'), ('Tm8', '11:30'), ('Tm9', '12:00'), ('Tm10', '12:30'), ('Tm11', '13:00'), ('Tm12', '13:30'), ('Tm13', '14:00'), ('Tm14', '14:30'), ('Tm15', '15:00'), ('Tm16', '15:30'), ('Tm17', '16:00'), ('Tm18', '16:30'), ('Tm19', '17:00')], default='Tm1', max_length=4),
        ),
        migrations.AddField(
            model_name='kitchen2register',
            name='sundayEndTime',
            field=models.CharField(choices=[('Tm1', '8:00'), ('Tm2', '8:30'), ('Tm3', '9:00'), ('Tm4', '9:30'), ('Tm5', '10:00'), ('Tm6', '10:30'), ('Tm7', '11:00'), ('Tm8', '11:30'), ('Tm9', '12:00'), ('Tm10', '12:30'), ('Tm11', '13:00'), ('Tm12', '13:30'), ('Tm13', '14:00'), ('Tm14', '14:30'), ('Tm15', '15:00'), ('Tm16', '15:30'), ('Tm17', '16:00'), ('Tm18', '16:30'), ('Tm19', '17:00')], default='Tm19', max_length=4),
        ),
        migrations.AddField(
            model_name='kitchen2register',
            name='sundayStartTime',
            field=models.CharField(choices=[('Tm1', '8:00'), ('Tm2', '8:30'), ('Tm3', '9:00'), ('Tm4', '9:30'), ('Tm5', '10:00'), ('Tm6', '10:30'), ('Tm7', '11:00'), ('Tm8', '11:30'), ('Tm9', '12:00'), ('Tm10', '12:30'), ('Tm11', '13:00'), ('Tm12', '13:30'), ('Tm13', '14:00'), ('Tm14', '14:30'), ('Tm15', '15:00'), ('Tm16', '15:30'), ('Tm17', '16:00'), ('Tm18', '16:30'), ('Tm19', '17:00')], default='Tm1', max_length=4),
        ),
        migrations.AddField(
            model_name='kitchen2register',
            name='thursdayEndTime',
            field=models.CharField(choices=[('Tm1', '8:00'), ('Tm2', '8:30'), ('Tm3', '9:00'), ('Tm4', '9:30'), ('Tm5', '10:00'), ('Tm6', '10:30'), ('Tm7', '11:00'), ('Tm8', '11:30'), ('Tm9', '12:00'), ('Tm10', '12:30'), ('Tm11', '13:00'), ('Tm12', '13:30'), ('Tm13', '14:00'), ('Tm14', '14:30'), ('Tm15', '15:00'), ('Tm16', '15:30'), ('Tm17', '16:00'), ('Tm18', '16:30'), ('Tm19', '17:00')], default='Tm19', max_length=4),
        ),
        migrations.AddField(
            model_name='kitchen2register',
            name='thursdayStartTime',
            field=models.CharField(choices=[('Tm1', '8:00'), ('Tm2', '8:30'), ('Tm3', '9:00'), ('Tm4', '9:30'), ('Tm5', '10:00'), ('Tm6', '10:30'), ('Tm7', '11:00'), ('Tm8', '11:30'), ('Tm9', '12:00'), ('Tm10', '12:30'), ('Tm11', '13:00'), ('Tm12', '13:30'), ('Tm13', '14:00'), ('Tm14', '14:30'), ('Tm15', '15:00'), ('Tm16', '15:30'), ('Tm17', '16:00'), ('Tm18', '16:30'), ('Tm19', '17:00')], default='Tm1', max_length=4),
        ),
        migrations.AddField(
            model_name='kitchen2register',
            name='tuesdayEndTime',
            field=models.CharField(choices=[('Tm1', '8:00'), ('Tm2', '8:30'), ('Tm3', '9:00'), ('Tm4', '9:30'), ('Tm5', '10:00'), ('Tm6', '10:30'), ('Tm7', '11:00'), ('Tm8', '11:30'), ('Tm9', '12:00'), ('Tm10', '12:30'), ('Tm11', '13:00'), ('Tm12', '13:30'), ('Tm13', '14:00'), ('Tm14', '14:30'), ('Tm15', '15:00'), ('Tm16', '15:30'), ('Tm17', '16:00'), ('Tm18', '16:30'), ('Tm19', '17:00')], default='Tm19', max_length=4),
        ),
        migrations.AddField(
            model_name='kitchen2register',
            name='tuesdayStartTime',
            field=models.CharField(choices=[('Tm1', '8:00'), ('Tm2', '8:30'), ('Tm3', '9:00'), ('Tm4', '9:30'), ('Tm5', '10:00'), ('Tm6', '10:30'), ('Tm7', '11:00'), ('Tm8', '11:30'), ('Tm9', '12:00'), ('Tm10', '12:30'), ('Tm11', '13:00'), ('Tm12', '13:30'), ('Tm13', '14:00'), ('Tm14', '14:30'), ('Tm15', '15:00'), ('Tm16', '15:30'), ('Tm17', '16:00'), ('Tm18', '16:30'), ('Tm19', '17:00')], default='Tm1', max_length=4),
        ),
        migrations.AddField(
            model_name='kitchen2register',
            name='wednesdayEndTime',
            field=models.CharField(choices=[('Tm1', '8:00'), ('Tm2', '8:30'), ('Tm3', '9:00'), ('Tm4', '9:30'), ('Tm5', '10:00'), ('Tm6', '10:30'), ('Tm7', '11:00'), ('Tm8', '11:30'), ('Tm9', '12:00'), ('Tm10', '12:30'), ('Tm11', '13:00'), ('Tm12', '13:30'), ('Tm13', '14:00'), ('Tm14', '14:30'), ('Tm15', '15:00'), ('Tm16', '15:30'), ('Tm17', '16:00'), ('Tm18', '16:30'), ('Tm19', '17:00')], default='Tm19', max_length=4),
        ),
        migrations.AddField(
            model_name='kitchen2register',
            name='wednesdayStartTime',
            field=models.CharField(choices=[('Tm1', '8:00'), ('Tm2', '8:30'), ('Tm3', '9:00'), ('Tm4', '9:30'), ('Tm5', '10:00'), ('Tm6', '10:30'), ('Tm7', '11:00'), ('Tm8', '11:30'), ('Tm9', '12:00'), ('Tm10', '12:30'), ('Tm11', '13:00'), ('Tm12', '13:30'), ('Tm13', '14:00'), ('Tm14', '14:30'), ('Tm15', '15:00'), ('Tm16', '15:30'), ('Tm17', '16:00'), ('Tm18', '16:30'), ('Tm19', '17:00')], default='Tm1', max_length=4),
        ),
    ]
