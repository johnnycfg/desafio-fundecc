from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from gestao_usuarios.models import Grupo, Usuario
from gestao_usuarios.serializer import GrupoSerializer, UsuarioSerializer

# Grupos
@api_view(['GET'])
def listar_grupos(request):
    grupos = Grupo.objects.all()
    serializer = GrupoSerializer(grupos, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def criar_grupo(request):
    serializer = GrupoSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    
# Usuários
@api_view(['GET'])
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def criar_usuario(request):
    serializer = UsuarioSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    



    
from rest_framework.views import APIView
from rest_framework import status

class GrupoList(APIView):
    def get(self, request):
        grupos = Grupo.objects.all()
        serializer = GrupoSerializer(grupos, many=True)
        
        return Response(serializer.data)

    def post(self, request):
        serializer = GrupoSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class GrupoDetail(APIView):
    def get_grupo_by_pk(self, pk):
        try:
            return Grupo.objects.get(pk=pk)
        except Grupo.DoesNotExist:
            print('caiu no except')
            return Response({
                'error': 'O grupo informado não existe'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        grupo = self.get_grupo_by_pk(pk)
        serializer = GrupoSerializer(grupo)

        return Response(serializer.data)
    
    def put(self, request, pk):
        grupo = self.get_grupo_by_pk(pk)
        serializer = GrupoSerializer(grupo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        grupo = self.get_grupo_by_pk(pk)
        grupo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UsuarioList(APIView):
    def get(self, request):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class UsuarioDetail(APIView):
    def get_usuario_by_pk(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
            
        except Usuario.DoesNotExist:
            return Response({
                'error': 'O usuario informado não existe'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        usuario = self.get_usuario_by_pk(pk)
        serializer = UsuarioSerializer(usuario)

        return Response(serializer.data)
    
    def put(self, request, pk):
        usuario = self.get_usuario_by_pk(pk)
        serializer = UsuarioSerializer(usuario, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        usuario = self.get_usuario_by_pk(pk)
        usuario.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
 