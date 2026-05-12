# Определяет сериализаторы для модели Note

from rest_framework import serializers
from django.utils.html import escape
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at', 'id']

    def validate_title(self, value):
        # Проверка наличия заголовка
        if not value.strip():
            raise serializers.ValidationError('Заголовок не может быть пустым')
        return escape(value)

    def validate_content(self, value):
        # Проверка наличия контента
        if not value.strip():
            raise serializers.ValidationError('Содержание не может быть пустым')
        return escape(value)

class NoteCreateSerializer(NoteSerializer):
    pass

class NoteUpdateSerializer(NoteSerializer):
    # Для обновления заметок, делает поля необязательными
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)

