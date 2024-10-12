# Generated by Django 5.1.2 on 2024-10-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_recipe_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='author',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='recipe',
            name='image_filter',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, default='../images/default_post_vlvmq3', upload_to='../images/'),
        ),
    ]
