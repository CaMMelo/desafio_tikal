from rest_framework import viewsets

from . import models, serializers


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer


class TelefoneViewSet(viewsets.ModelViewSet):
    queryset = models.Telefone.objects.all()
    serializer_class = serializers.TelefoneSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = models.Email.objects.all()
    serializer_class = serializers.EmailSerializer
