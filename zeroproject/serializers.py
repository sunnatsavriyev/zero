from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import (
    MahsulotKategoriya, MahsulotBrend, Mahsulot, Ombor, YetkazibBeruvchi,
    OmborKirim, OmborChiqim, MahsulotNarxi, MahsulotSoni, OmborKochirish,
    Xarajat, KassaKirim, Buyurtma, BuyurtmaMahsulot, Tolov, Filial, NarxSozlamalari
)

User = get_user_model()

# --- User (minimal) ---
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "role", "is_superuser")


# --- Mahsulotlar ---
class MahsulotKategoriyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MahsulotKategoriya
        fields = "__all__"


class MahsulotBrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = MahsulotBrend
        fields = "__all__"


class MahsulotSerializer(serializers.ModelSerializer):
    kategoriya = MahsulotKategoriyaSerializer(read_only=True)
    kategoriya_id = serializers.PrimaryKeyRelatedField(
        queryset=MahsulotKategoriya.objects.all(), source="kategoriya", write_only=True, required=False
    )
    brend = MahsulotBrendSerializer(read_only=True)
    brend_id = serializers.PrimaryKeyRelatedField(
        queryset=MahsulotBrend.objects.all(), source="brend", write_only=True, required=False
    )

    class Meta:
        model = Mahsulot
        fields = [
            "id", "nomi", "kategoriya", "kategoriya_id", "brend", "brend_id",
            "status", "izoh", "rasm"
        ]


# --- Ombor va yetkazib beruvchi ---
class OmborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ombor
        fields = "__all__"


class YetkazibBeruvchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = YetkazibBeruvchi
        fields = "__all__"


class OmborKirimSerializer(serializers.ModelSerializer):
    class Meta:
        model = OmborKirim
        fields = "__all__"


class OmborChiqimSerializer(serializers.ModelSerializer):
    class Meta:
        model = OmborChiqim
        fields = "__all__"


class OmborKochirishSerializer(serializers.ModelSerializer):
    class Meta:
        model = OmborKochirish
        fields = "__all__"


class MahsulotNarxiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MahsulotNarxi
        fields = "__all__"


class MahsulotSoniSerializer(serializers.ModelSerializer):
    class Meta:
        model = MahsulotSoni
        fields = "__all__"


# --- Kassa ---
class XarajatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xarajat
        fields = "__all__"


class KassaKirimSerializer(serializers.ModelSerializer):
    class Meta:
        model = KassaKirim
        fields = "__all__"


# --- Buyurtma / Sotuv ---
class BuyurtmaMahsulotSerializer(serializers.ModelSerializer):
    mahsulot = MahsulotSerializer(read_only=True)
    mahsulot_id = serializers.PrimaryKeyRelatedField(
        queryset=Mahsulot.objects.all(), source="mahsulot", write_only=True
    )

    class Meta:
        model = BuyurtmaMahsulot
        fields = ["id", "buyurtma", "mahsulot", "mahsulot_id", "soni", "narx"]


class BuyurtmaSerializer(serializers.ModelSerializer):
    items = BuyurtmaMahsulotSerializer(many=True, read_only=True)

    class Meta:
        model = Buyurtma
        fields = ["id", "mijoz_ismi", "mijoz_telefoni", "sana", "kassir", "items"]


class TolovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tolov
        fields = "__all__"


# --- Filial / Narx sozlamalari ---
class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = "__all__"


class NarxSozlamalariSerializer(serializers.ModelSerializer):
    class Meta:
        model = NarxSozlamalari
        fields = "__all__"
