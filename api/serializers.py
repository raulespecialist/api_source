from .models import Email
from rest_framework import serializers


class EmailSerializer(serializers.HyperlinkedModelSerializer):


    valid_email = serializers.SerializerMethodField(method_name='conversion_bool')
    fraud = serializers.SerializerMethodField(method_name='conversion_boolfraud')

    class Meta:
        model = Email
        fields = ['email', 'creation_date', 'email_status', 'email_score', 'valid_email', 'fraud']

    def conversion_bool(self, instance):
        if instance.valid_email == True:
            return 1
        else:
            return 0

    def conversion_boolfraud(self, instance):
        if instance.fraud == True:
            return 1
        else:
            return 0

class EmailListSerializer(serializers.HyperlinkedModelSerializer):


    valid_email = serializers.SerializerMethodField(method_name='conversion_bool')
    fraud = serializers.SerializerMethodField(method_name='conversion_boolfraud')

    class Meta:
        model = Email
        fields = ['email', 'creation_date', 'email_status', 'email_score', 'valid_email', 'fraud']

    def conversion_bool(self, instance):
        if instance.valid_email == True:
            return 1
        else:
            return 0

    def conversion_boolfraud(self, instance):
        if instance.fraud == True:
            return 1
        else:
            return 0