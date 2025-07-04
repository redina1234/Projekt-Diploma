# Generated by Django 5.2 on 2025-06-28 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ingredients", "0001_initial"),
        ("recipes", "0005_remove_recipe_nutritional_info_recipe_calories_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecipeIngredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Quantity needed for this recipe",
                        max_digits=8,
                    ),
                ),
                (
                    "unit",
                    models.CharField(help_text="Unit of measurement", max_length=50),
                ),
                (
                    "notes",
                    models.TextField(
                        blank=True,
                        help_text="Additional notes for this ingredient",
                        null=True,
                    ),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ingredients.ingredient",
                    ),
                ),
                (
                    "recipe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="recipes.recipe"
                    ),
                ),
            ],
            options={
                "verbose_name": "Recipe Ingredient",
                "verbose_name_plural": "Recipe Ingredients",
                "unique_together": {("recipe", "ingredient")},
            },
        ),
    ]
