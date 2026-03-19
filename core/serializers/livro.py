from rest_framework.serializers import ModelSerializer

from core.models import Livro


class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
