# Generated by Django 2.1.1 on 2018-11-23 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0103_auto_20181121_1224'),
        ('ticketoutputpdf', '0006_auto_20181017_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketlayoutitem',
            name='sales_channel',
            field=models.CharField(default='web', max_length=190),
        ),
        migrations.AlterField(
            model_name='ticketlayoutitem',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticketlayout_assignments', to='pretixbase.Item'),
        ),
        migrations.AlterUniqueTogether(
            name='ticketlayoutitem',
            unique_together={('item', 'layout', 'sales_channel')},
        ),
    ]
