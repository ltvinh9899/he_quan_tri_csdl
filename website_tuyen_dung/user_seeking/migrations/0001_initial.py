# Generated by Django 3.1.2 on 2020-10-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(max_length=20)),
                ('user_type_id', models.IntegerField(max_length=10)),
                ('email_user', models.EmailField(max_length=255)),
                ('password_user', models.CharField(max_length=255)),
            ],
        ),
    ]
