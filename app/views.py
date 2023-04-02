from rest_framework import generics
from .models import Servico, Funcionario
from .serializers import ServicoSerializer, FuncionarioSerializer

# usando a generics do rest framework para poder usar PUT, GET, POST e DELETE 
# tanto de serviços quanto de funcionários

class ServicoList(generics.ListCreateAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class ServicoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class FuncionarioList(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class FuncionarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer