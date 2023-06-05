from rest_framework import serializers
from gestao_usuarios.models import Grupo, Usuario
    
class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = "__all__"

    def validate(self, data):
        if data['status'] not in ['Ativo', 'Inativo']:
            raise serializers.ValidationError("Valor inválido para o campo status")
        return data

class UsuarioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome_completo = serializers.CharField()
    idade = serializers.IntegerField()
    sexo = serializers.CharField()
    email = serializers.EmailField()
    telefone = serializers.CharField()
    pais = serializers.CharField()
    estado = serializers.CharField()
    cidade = serializers.CharField()
    bairro = serializers.CharField()
    logradouro = serializers.CharField()
    status = serializers.CharField()
    grupo = serializers.PrimaryKeyRelatedField(queryset=Grupo.objects.all())

    def validate(self, data):
        if data['status'] not in ['Ativo', 'Inativo']:
            raise serializers.ValidationError("Valor inválido para o campo status")
        return data

    def create(self, data):
        return Usuario.objects.create(**data)
    
    def update(self, instance, validated_data):
        instance.nome_completo = validated_data.get('nome_completo', instance.nome_completo)
        instance.idade = validated_data.get('idade', instance.idade)
        instance.sexo = validated_data.get('sexo', instance.sexo)
        instance.email = validated_data.get('email', instance.email)
        instance.telefone = validated_data.get('telefone', instance.telefone)
        instance.pais = validated_data.get('pais', instance.pais)
        instance.estado = validated_data.get('estado', instance.estado)
        instance.cidade = validated_data.get('cidade', instance.cidade)
        instance.bairro = validated_data.get('bairro', instance.bairro)
        instance.logradouro = validated_data.get('logradouro', instance.logradouro)
        instance.status = validated_data.get('status', instance.status)
        instance.grupo = validated_data.get('grupo', instance.grupo)
        instance.save()
        return instance