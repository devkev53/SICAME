# Generated by Django 2.2.5 on 2019-10-10 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0014_delete_material_detalle_egreso'),
        ('movimientos', '0019_remove_asignacion_devuelto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo_Asignado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_asignacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movimientos.Asignacion', verbose_name='Ingreso')),
                ('id_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Equipo_Ingreso', verbose_name='Equipo')),
            ],
            options={
                'verbose_name': 'Equipo_Asignado',
                'verbose_name_plural': 'Equipo_Asignados',
            },
        ),
    ]
