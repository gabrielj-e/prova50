from django.db import models


# Equivalente à sua tabela 'Regras'
class Regra(models.Model):
    TIPO_CHOICES = [
        ('Verbal', 'Verbal'),
        ('Nominal', 'Nominal'),
    ]

    descricao = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.tipo}: {self.descricao}"


# Equivalente à sua tabela 'Nucleos'
class Nucleo(models.Model):
    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino'),
        ('N/A', 'N/A'),
    ]
    NUMERO_CHOICES = [
        ('Singular', 'Singular'),
        ('Plural', 'Plural'),
    ]
    PESSOA_CHOICES = [
        ('1a', '1a'),
        ('2a', '2a'),
        ('3a', '3a'),
        ('N/A', 'N/A'),
    ]

    termo = models.CharField(max_length=100)
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, default='N/A')
    numero = models.CharField(max_length=10, choices=NUMERO_CHOICES)
    pessoa = models.CharField(max_length=3, choices=PESSOA_CHOICES, default='N/A')

    def __str__(self):
        return self.termo


# Equivalente à sua tabela 'Elementos_Flexionados'
class ElementoFlexionado(models.Model):
    # Reutilizando as choices de Nucleo para consistência
    termo = models.CharField(max_length=100)
    genero = models.CharField(max_length=10, choices=Nucleo.GENERO_CHOICES, default='N/A')
    numero = models.CharField(max_length=10, choices=Nucleo.NUMERO_CHOICES)
    pessoa = models.CharField(max_length=3, choices=Nucleo.PESSOA_CHOICES, default='N/A')

    def __str__(self):
        return self.termo


# Equivalente à sua tabela 'Mapeamentos' (com as ForeignKeys)
class Mapeamento(models.Model):
    # O Django cria as ForeignKeys automaticamente
    nucleo = models.ForeignKey(Nucleo, on_delete=models.CASCADE)
    elemento = models.ForeignKey(ElementoFlexionado, on_delete=models.CASCADE)
    regra = models.ForeignKey(Regra, on_delete=models.CASCADE)
    frase_exemplo = models.CharField(max_length=255)

    def __str__(self):
        return self.frase_exemplo


from django.db import models

# Create your models here.
