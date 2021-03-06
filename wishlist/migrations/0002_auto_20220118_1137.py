# Generated by Django 3.2.7 on 2022-01-18 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='name',
            field=models.CharField(blank=True, default='My Wishlist', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='products.Product'),
        ),
        migrations.CreateModel(
            name='WishListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='wishitems', to='wishlist.wishlist')),
            ],
        ),
    ]
