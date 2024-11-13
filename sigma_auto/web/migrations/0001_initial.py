# Generated by Django 5.1.3 on 2024-11-13 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('cpf', models.CharField(max_length=14)),
                ('nome', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=20)),
                ('renda', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Montadora',
            fields=[
                ('id_montadora', models.AutoField(primary_key=True, serialize=False)),
                ('cnpj', models.CharField(max_length=20)),
                ('razao_social', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=50)),
                ('contato', models.CharField(max_length=50)),
                ('tel_comercial', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id_veiculo', models.AutoField(primary_key=True, serialize=False)),
                ('chassi', models.CharField(max_length=17)),
                ('placa', models.CharField(max_length=10)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('ano_fab', models.IntegerField()),
                ('ano_modelo', models.IntegerField()),
                ('cor', models.CharField(max_length=20)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id_vendedor', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField()),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id_endereco', models.AutoField(primary_key=True, serialize=False)),
                ('cep', models.CharField(max_length=10)),
                ('rua', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('modelo', models.CharField(max_length=50)),
                ('ano', models.IntegerField()),
                ('cor', models.CharField(max_length=20)),
                ('acessorios', models.TextField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.cliente')),
                ('montadora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.montadora')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='OperacaoDeVenda',
            fields=[
                ('id_operacao_venda', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('data', models.DateField()),
                ('valor_entrada', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_financiado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.cliente')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.veiculo')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.vendedor')),
            ],
        ),
        migrations.CreateModel(
            name='OperacaoDeCompra',
            fields=[
                ('id_operacao_compra', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('data', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.cliente')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.veiculo')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.vendedor')),
            ],
        ),
    ]