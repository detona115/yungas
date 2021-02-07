from django.urls import path
from .views import PessoaAPIView, RegiaoAPIView, PessoaHomeView

urlpatterns = [
    path('', PessoaHomeView.as_view()),
    path('api/', PessoaAPIView.as_view(), name='main'),    
    path('api/regiao/<slug:pk>', RegiaoAPIView.as_view(), name='regiao'),    
]
