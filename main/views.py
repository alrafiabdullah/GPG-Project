from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.exceptions import ValidationError

from .models import Payload
from .serializers import PayloadSerializer

import gnupg
# Create your views here.


def index(request):
    return render(request, "main/index.html")


class PayloadList(ListAPIView):
    queryset = Payload.objects.all()
    serializer_class = PayloadSerializer


class PostPayloadView(CreateAPIView):
    serializer_class = PayloadSerializer

    def get_queryset(self):
        payload = Payload.objects.all()
        return payload

    def create(self, request, *args, **kwargs):
        gpg = gnupg.GPG()
        gpg.encoding = "utf-8"

        try:
            passphrase = request.data.get("passphrase")
            message = request.data.get("message")
            status = gpg.decrypt(
                str(message), passphrase=str(passphrase))

        except:
            raise ValidationError({
                "Error": "A valid input for both field is required!"
            })

        if str(status) == "":
            return Response({"Error": "Please check the newlines of the encrypted message!"}, status=400)

        return Response({"DecryptedMessage": "The given message, decrypted using GPG and the given passphrase"}, status=200)
