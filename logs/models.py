from django.db import models
from rest_framework import serializers


class MetaDataModel(models.Model):
    parentResourceId = models.TextField()

    class Meta:
        db_table = 'metadata'

    def __str__(self):
        ans = '{ "parentResourceId": "' + self.parentResourceId + '" }'
        return ans


class LogModel(models.Model):
    level = models.TextField()
    message = models.TextField()
    resourceId = models.TextField()
    timestamp = models.DateTimeField()
    traceId = models.TextField()
    spanId = models.TextField()
    commit = models.TextField()
    metadata = models.ForeignKey(MetaDataModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'log'


class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaDataModel
        fields = ['parentResourceId']


class LogSerializer(serializers.ModelSerializer):
    metadata = MetaDataSerializer()

    class Meta:
        model = LogModel
        fields = '__all__'

    def create(self, validated_data):
        metadata_data = validated_data.pop('metadata')
        metadata = MetaDataModel.objects.create(
            **metadata_data
        )
        log = LogModel.objects.create(metadata=metadata, **validated_data)
        return log
