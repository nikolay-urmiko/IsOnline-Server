# Generated by Django 2.2.12 on 2020-04-27 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ur_face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ur_face_name', models.CharField(max_length=100, verbose_name='Наименование Юридического лица')),
            ],
            options={
                'verbose_name': 'Юридическое лицо',
                'verbose_name_plural': 'Юридические лица',
                'ordering': ('ur_face_name',),
            },
        ),
        migrations.CreateModel(
            name='Checks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namedot', models.CharField(max_length=100, verbose_name='название точки')),
                ('last_online', models.DateTimeField(verbose_name='дата последнего соединения')),
                ('GOST_key', models.DateTimeField(verbose_name='дата окончания ключа ГОСТ')),
                ('ur_facce', models.ForeignKey(on_delete='CASKADE', to='Check.Ur_face')),
            ],
            options={
                'verbose_name': 'Торговая точка',
                'verbose_name_plural': 'Торговые точки',
                'ordering': ('namedot',),
            },
        ),
    ]