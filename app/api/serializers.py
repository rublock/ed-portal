from rest_framework import serializers
from mainapp import models as mainapp_models


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "title",
            "preambule",
            "body",
            "created",
            "updated",
            "deleted",
        )
        model = mainapp_models.News
