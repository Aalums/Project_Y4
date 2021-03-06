# Generated by Django 3.0.3 on 2020-04-21 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_auto_20200421_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_info',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('age', models.IntegerField(default=0)),
                ('BMI', models.DecimalField(decimal_places=2, max_digits=20)),
                ('DM', models.IntegerField(default=0)),
                ('HT', models.IntegerField(default=0)),
                ('DLP', models.IntegerField(default=0)),
                ('CKD', models.IntegerField(default=0)),
                ('LAD4dmspect', models.DecimalField(decimal_places=2, max_digits=20)),
                ('LADwallthick', models.DecimalField(decimal_places=2, max_digits=20)),
                ('LADwallmotion', models.DecimalField(decimal_places=2, max_digits=20)),
                ('LADCAG', models.IntegerField(default=0)),
                ('LCX4dmspect', models.DecimalField(decimal_places=2, max_digits=20)),
                ('LCXwallthick', models.DecimalField(decimal_places=2, max_digits=20)),
                ('LCXwallmotion', models.DecimalField(decimal_places=2, max_digits=20)),
                ('LCXCAG', models.IntegerField(default=0)),
                ('RCA4dmspect', models.DecimalField(decimal_places=2, max_digits=20)),
                ('RCAwallthick', models.DecimalField(decimal_places=2, max_digits=20)),
                ('RCAwallmotion', models.DecimalField(decimal_places=2, max_digits=20)),
                ('RCACAG', models.IntegerField(default=0)),
                ('LVEF', models.IntegerField(default=0)),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patients')),
            ],
        ),
    ]
