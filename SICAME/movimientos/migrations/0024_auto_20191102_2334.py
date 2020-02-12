# Generated by Django 2.2.5 on 2019-11-03 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movimientos', '0023_auto_20191028_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mi_Asignacion',
            fields=[
            ],
            options={
                'verbose_name': 'Mi Asignacion',
                'verbose_name_plural': 'Mis Asignaciones',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('movimientos.asignacion',),
        ),
        migrations.AlterModelOptions(
            name='asignacion',
            options={'ordering': ['-fecha', '-hora'], 'verbose_name': 'Asignacion', 'verbose_name_plural': 'Asignaciones'},
        ),
        migrations.AlterModelOptions(
            name='devolucion',
            options={'ordering': ['-fecha', '-hora'], 'verbose_name': 'Devolucion', 'verbose_name_plural': 'Devoluciones'},
        ),
        migrations.AlterField(
            model_name='equipo_devuelto',
            name='comentarios',
            field=models.TextField(blank=True, verbose_name='Comentarios'),
        ),
        migrations.AlterField(
            model_name='equipo_devuelto',
            name='id_equipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Equipo_for_asig', verbose_name='Equipo'),
        ),
        migrations.AlterField(
            model_name='material_asignado',
            name='ubicacion',
            field=models.CharField(max_length=75, verbose_name='Ubicacion'),
        ),
    ]