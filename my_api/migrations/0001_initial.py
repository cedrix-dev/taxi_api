# Generated by Django 3.1.4 on 2020-12-31 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emmeteurMessage', models.CharField(max_length=200)),
                ('recepteurMessage', models.CharField(max_length=200)),
                ('dateEnvoie', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='objetPerdu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('date_de_perte', models.DateField()),
                ('date_de_remise', models.DateField()),
                ('heure_perte', models.TimeField()),
                ('heure_remise', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='personne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=4)),
                ('lieuResidence', models.CharField(max_length=200)),
                ('sexe', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='passager',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_api.personne')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('message', models.ManyToManyField(to='my_api.Message')),
            ],
            bases=('my_api.personne',),
        ),
        migrations.CreateModel(
            name='taximan',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_api.personne')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('etattaximan', models.CharField(max_length=200)),
            ],
            bases=('my_api.personne',),
        ),
        migrations.CreateModel(
            name='reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateReservation', models.DateField()),
                ('etatReservation', models.CharField(max_length=200)),
                ('passsager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_api.passager')),
                ('taximan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_api.taximan')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='taximan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_api.taximan'),
        ),
        migrations.CreateModel(
            name='declarationDePerte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptionObjectPerdu', models.CharField(max_length=200)),
                ('reservation', models.CharField(max_length=200)),
                ('passager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_api.passager')),
            ],
        ),
        migrations.CreateModel(
            name='administrateur',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='my_api.personne')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('declaration', models.ManyToManyField(to='my_api.declarationDePerte')),
                ('message', models.ManyToManyField(to='my_api.Message')),
                ('objetperdu', models.ManyToManyField(to='my_api.objetPerdu')),
            ],
            bases=('my_api.personne',),
        ),
    ]
