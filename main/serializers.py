from rest_framework import serializers

from .models import Payload


class PayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payload
        fields = ("id", "passphrase", "message", "decrypted_message")
        read_only_fields = ("decrypted_message",)
