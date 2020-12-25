from rest_framework import serializers

class InputSerializer(serializers.Serializer):
    project_name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=20)

