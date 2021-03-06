from rest_framework import generics, permissions

from pessoas.models import Fone
from pessoas.serializers import FoneSerializer

class FoneList(generics.ListAPIView):
    """Listando todos os fones"""
    queryset = Fone.objects.all()
    serializer_class = FoneSerializer
    permission_classes = ()


class FoneDestroy(generics.DestroyAPIView):
    """Excluindo fone"""
    queryset = Fone.objects.all()
    serializer_class = FoneSerializer
    permission_classes = (
        permissions.IsAdminUser,
    )


class FoneUpdate(generics.UpdateAPIView):
    """Update de fone"""
    queryset = Fone.objects.all()
    serializer_class = FoneSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class FoneCreate(generics.CreateAPIView):
    """Criando fone"""
    queryset = Fone.objects.all()
    serializer_class = FoneSerializer
    permission_classes = (
        permissions.DjangoModelPermissions,
    )


class FoneGet(generics.RetrieveAPIView):
    """Listando um fone"""
    queryset = Fone.objects.all()
    serializer_class = FoneSerializer
    permission_classes = ()