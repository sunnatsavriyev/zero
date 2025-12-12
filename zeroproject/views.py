from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model

from .models import *
from .serializers import *
from .permissions import IsRoleAllowed

User = get_user_model()

# --- Mahsulotlar ---
class MahsulotKategoriyaViewSet(viewsets.ModelViewSet):
    queryset = MahsulotKategoriya.objects.all()
    serializer_class = MahsulotKategoriyaSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["manager", "admin"]  # who can create/edit/delete


class MahsulotBrendViewSet(viewsets.ModelViewSet):
    queryset = MahsulotBrend.objects.all()
    serializer_class = MahsulotBrendSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["manager", "admin"]


class MahsulotViewSet(viewsets.ModelViewSet):
    queryset = Mahsulot.objects.select_related("kategoriya", "brend").all()
    serializer_class = MahsulotSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["manager", "omborchi"]  # e.g., omborchi can add products
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["kategoriya", "brend", "status"]
    search_fields = ["nomi", "izoh"]


# --- Ombor bo‘limi ---
class OmborViewSet(viewsets.ModelViewSet):
    queryset = Ombor.objects.all()
    serializer_class = OmborSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["manager"]


class YetkazibBeruvchiViewSet(viewsets.ModelViewSet):
    queryset = YetkazibBeruvchi.objects.all()
    serializer_class = YetkazibBeruvchiSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["manager", "omborchi"]


class OmborKirimViewSet(viewsets.ModelViewSet):
    queryset = OmborKirim.objects.all()
    serializer_class = OmborKirimSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["omborchi"]


class OmborChiqimViewSet(viewsets.ModelViewSet):
    queryset = OmborChiqim.objects.all()
    serializer_class = OmborChiqimSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["omborchi"]


class OmborKochirishViewSet(viewsets.ModelViewSet):
    queryset = OmborKochirish.objects.all()
    serializer_class = OmborKochirishSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["omborchi"]


class MahsulotNarxiViewSet(viewsets.ModelViewSet):
    queryset = MahsulotNarxi.objects.all()
    serializer_class = MahsulotNarxiSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["manager", "omborchi"]


class MahsulotSoniViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MahsulotSoni.objects.select_related("mahsulot", "ombor").all()
    serializer_class = MahsulotSoniSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["omborchi", "manager"]


# --- Kassa ---
class XarajatViewSet(viewsets.ModelViewSet):
    queryset = Xarajat.objects.all()
    serializer_class = XarajatSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["kassir"]


class KassaKirimViewSet(viewsets.ModelViewSet):
    queryset = KassaKirim.objects.all()
    serializer_class = KassaKirimSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["kassir"]


# --- Buyurtma / sotuv ---
class BuyurtmaViewSet(viewsets.ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["kassir"]


class BuyurtmaMahsulotViewSet(viewsets.ModelViewSet):
    queryset = BuyurtmaMahsulot.objects.all()
    serializer_class = BuyurtmaMahsulotSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["kassir"]


class TolovViewSet(viewsets.ModelViewSet):
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["kassir"]


# --- Filial / narx sozlamalari ---
class FilialViewSet(viewsets.ModelViewSet):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["manager"]


class NarxSozlamalariViewSet(viewsets.ModelViewSet):
    queryset = NarxSozlamalari.objects.all()
    serializer_class = NarxSozlamalariSerializer
    permission_classes = [IsRoleAllowed]
    allowed_roles = ["manager"]
