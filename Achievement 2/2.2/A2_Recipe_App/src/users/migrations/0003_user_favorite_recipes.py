# Generated by Django 4.2.6 on 2023-10-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_alter_recipe_cooking_instructions_and_more'),
        ('users', '0002_remove_user_favorite_recipes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_recipes',
            field=models.ManyToManyField(to='recipes.recipe'),
        ),
    ]
