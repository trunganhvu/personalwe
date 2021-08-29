# Generated by Django 3.2.4 on 2021-08-29 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210829_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False)),
                ('delivery_name', models.CharField(max_length=100)),
                ('delivery_phone', models.CharField(max_length=25)),
                ('delivery_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('is_using', models.BooleanField(default=False)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_name', models.CharField(max_length=255)),
                ('event_note', models.CharField(max_length=1000)),
                ('event_slogun', models.CharField(max_length=500)),
                ('event_description', models.CharField(max_length=1000)),
                ('event_image_banner', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('event_start', models.DateField(null=True)),
                ('event_end', models.DateField(null=True)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=1000)),
                ('order_code', models.CharField(max_length=1000)),
                ('order_note', models.CharField(max_length=1000)),
                ('order_time', models.DateField()),
                ('confirm_order_status', models.BooleanField(default=False)),
                ('confirm_order_time', models.DateField(null=True)),
                ('delivery_customer_pay', models.DecimalField(decimal_places=2, max_digits=12)),
                ('delivery_shop_pay', models.DecimalField(decimal_places=2, max_digits=12)),
                ('delivery_status', models.BooleanField(default=False)),
                ('delivery_time', models.DateField(null=True)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
                ('delivery_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.delivery')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_code', models.CharField(max_length=25)),
                ('product_name', models.CharField(max_length=255)),
                ('product_description', models.CharField(max_length=1000)),
                ('product_detail', models.CharField(max_length=1000)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductColor',
            fields=[
                ('product_color_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_color_code', models.CharField(max_length=255)),
                ('product_color_name', models.CharField(max_length=255)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('product_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_type_code', models.CharField(max_length=25)),
                ('product_type_name', models.CharField(max_length=255)),
                ('product_type_description', models.CharField(max_length=1000)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('product_size_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_size_code', models.CharField(max_length=25)),
                ('product_size_name', models.CharField(max_length=255)),
                ('product_size_height_max', models.IntegerField(default=0)),
                ('product_size_height_min', models.IntegerField(default=0)),
                ('product_size_width_max', models.IntegerField(default=0)),
                ('product_size_width_min', models.IntegerField(default=0)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
                ('product_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.producttype')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPromotion',
            fields=[
                ('product_promotion_id', models.AutoField(primary_key=True, serialize=False)),
                ('discount', models.IntegerField(default=0)),
                ('product_promotion_start', models.DateField()),
                ('product_promotion_end', models.DateField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.event')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('product_image_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_image_name', models.CharField(max_length=255)),
                ('product_image_path', models.CharField(max_length=255)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('product_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('number_of_product', models.IntegerField(default=0)),
                ('product_original_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('product_public_price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
                ('product_color_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcolor')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product')),
                ('product_size_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productsize')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.producttype'),
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('order_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.order')),
                ('product_detail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productdetail')),
            ],
        ),
    ]
