from django.db import models


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    renda = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class Vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key=True)
    codigo = models.IntegerField()
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Montadora(models.Model):
    id_montadora = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=20)
    razao_social = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    contato = models.CharField(max_length=50)
    tel_comercial = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)

    def __str__(self):
        return self.razao_social


class Veiculo(models.Model):
    id_veiculo = models.AutoField(primary_key=True)
    chassi = models.CharField(max_length=17)
    placa = models.CharField(max_length=10)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano_fab = models.IntegerField()
    ano_modelo = models.IntegerField()
    cor = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(blank=True, upload_to='veiculos/')

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.placa})'


class Endereco(models.Model):
    id_endereco = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.rua}, {self.numero}, {self.cidade} - {self.estado}'


class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)
    data = models.DateField()
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    cor = models.CharField(max_length=20)
    acessorios = models.TextField()

    def __str__(self):
        return f'Pedido {self.id_pedido} - {self.modelo}'


class OperacaoDeVenda(models.Model):
    id_operacao_venda = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    numero = models.IntegerField()
    data = models.DateField()
    valor_entrada = models.DecimalField(max_digits=10, decimal_places=2)
    valor_financiado = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Operação de Venda {self.id_operacao_venda}'


class OperacaoDeCompra(models.Model):
    id_operacao_compra = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    numero = models.IntegerField()
    data = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Operação de Compra {self.id_operacao_compra}'
