from django.db import models

# duas entidades, com relação de 1 para 1 entre eles
# testei com o Insomnia, e é possível tanto consultar qual o barbeiro de um corte específico 
# quanto quais os serviços estão atrelados a um barbeiro 

class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=100, verbose_name="Barbeiro:")
    telefone_funcionario = models.CharField(max_length=20, verbose_name="Fone Barbeiro:", default="1111-1111")

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    barbeiro = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    def __str__(self):
        return self.name