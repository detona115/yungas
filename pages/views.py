from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from help import seed_db
from .models import Pessoa

# api
from rest_framework import generics
from .serializers import PessoaSerializer
from .pagination import CustomLimitOffsetPagination, CustomPageNumberPagination

class PessoaHomeView(TemplateView):
    template_name = 'home.html'

class PessoaAPIView(generics.ListAPIView):
       
    serializer_class = PessoaSerializer
    pagination_class = CustomPageNumberPagination #PageNumberPagination
    def get_queryset(self): 
        seed_db()        
        return Pessoa.objects.all()

class RegiaoAPIView(generics.ListAPIView):    

    serializer_class = PessoaSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):  
              
        return Pessoa.objects.filter(regiao=self.kwargs['pk'])
    
    
    
