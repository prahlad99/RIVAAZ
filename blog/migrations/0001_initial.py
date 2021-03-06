# Generated by Django 3.1.7 on 2021-06-26 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=60)),
                ('head0', models.CharField(default='', max_length=400)),
                ('head1', models.CharField(default='', max_length=400)),
                ('head2', models.CharField(default='', max_length=400)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
