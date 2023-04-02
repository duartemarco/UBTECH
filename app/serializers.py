from rest_framework import serializers
from app.models import Funcionario, Servico

# serializador de serviços
class ServicoSerializer (serializers.ModelSerializer):
     class Meta:
         model = Servico
         fields = ['nome', 'preco', 'barbeiro']

# serializador de funcionários
class FuncionarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['nome_funcionario', 'telefone_funcionario', 'id']