# Generated by Django 5.2 on 2025-05-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_delete_category_delete_ingredient_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='preparation_method',
            new_name='preparation_steps',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_number',
        ),
        migrations.AddField(
            model_name='recipe',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipes/images/'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='course_type',
            field=models.CharField(choices=[('appetizer', 'Appetizer'), ('main_course', 'Main Course'), ('soup', 'Soup'), ('salad', 'Salad'), ('dessert', 'Dessert')], max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='nutritional_info',
            field=models.TextField(),
        ),
    ]
