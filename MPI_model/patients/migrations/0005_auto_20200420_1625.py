# Generated by Django 3.0.3 on 2020-04-20 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_auto_20200414_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient_info',
            fields=[
                ('info_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('age', models.IntegerField()),
                ('bmi', models.DecimalField(decimal_places=2, max_digits=20)),
                ('dm', models.BinaryField()),
                ('ht', models.BinaryField()),
                ('dlp', models.BinaryField()),
                ('ckd', models.BinaryField()),
                ('LAD_4dmspect', models.DecimalField(decimal_places=2, max_digits=20)),
                ('LAD_wallthick', models.DecimalField(decimal_places=2, max_digits=20)),
                ('LAD_wallmotion', models.DecimalField(decimal_places=2, max_digits=20)),
                ('LAD_CAG', models.BinaryField()),
                ('LCX_4dmspect', models.DecimalField(decimal_places=2, max_digits=20)),
                ('LCX_wallthick', models.DecimalField(decimal_places=2, max_digits=20)),
                ('LCX_wallmotion', models.DecimalField(decimal_places=2, max_digits=20)),
                ('LCX_CAG', models.BinaryField()),
                ('RCA_4dmspect', models.DecimalField(decimal_places=2, max_digits=20)),
                ('RCA_wallthick', models.DecimalField(decimal_places=2, max_digits=20)),
                ('RCA_wallmotion', models.DecimalField(decimal_places=2, max_digits=20)),
                ('RCA_CAG', models.BinaryField()),
                ('LVEF', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='patient_mpi',
            name='char_id',
        ),
        migrations.AlterField(
            model_name='patients',
            name='gender',
            field=models.BinaryField(),
        ),
        migrations.DeleteModel(
            name='patient_characteristic',
        ),
        migrations.DeleteModel(
            name='patient_mpi',
        ),
        migrations.AddField(
            model_name='patient_info',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patients'),
        ),
    ]