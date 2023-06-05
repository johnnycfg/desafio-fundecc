from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from gestao_usuarios.views import GrupoList, GrupoDetail, UsuarioList, UsuarioDetail


urlpatterns = [
    path('grupos/', GrupoList.as_view()),
    path('grupos/<int:pk>', GrupoDetail.as_view()),
    path('usuarios/', UsuarioList.as_view()),
    path('usuarios/<int:pk>', UsuarioDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
