from django.contrib import admin
from .models import (
    MahsulotKategoriya, MahsulotBrend, Mahsulot, Ombor, YetkazibBeruvchi,
    OmborKirim, OmborChiqim, MahsulotNarxi, MahsulotSoni, OmborKochirish,
    Xarajat, KassaKirim, Buyurtma, BuyurtmaMahsulot, Tolov, Filial, NarxSozlamalari
)

@admin.register(MahsulotKategoriya)
class MahsulotKategoriyaAdmin(admin.ModelAdmin):
    list_display = ("id", "nomi", "status")
    search_fields = ("nomi",)
    list_filter = ("status",)


@admin.register(MahsulotBrend)
class MahsulotBrendAdmin(admin.ModelAdmin):
    list_display = ("id", "nomi", "status")
    search_fields = ("nomi",)


@admin.register(Mahsulot)
class MahsulotAdmin(admin.ModelAdmin):
    list_display = ("id", "nomi", "kategoriya", "brend", "status")
    list_filter = ("status", "kategoriya", "brend")
    search_fields = ("nomi",)
    readonly_fields = ("id",)


@admin.register(Ombor)
class OmborAdmin(admin.ModelAdmin):
    list_display = ("id", "nomi", "filial", "status")
    list_filter = ("status",)


@admin.register(YetkazibBeruvchi)
class YetkazibBeruvchiAdmin(admin.ModelAdmin):
    list_display = ("id", "nomi", "telefon", "status")
    search_fields = ("nomi", "rasmiy_nomi")


@admin.register(OmborKirim)
class OmborKirimAdmin(admin.ModelAdmin):
    list_display = ("id", "mahsulot", "ombor", "miqdor", "yetkazib_beruvchi", "sana")
    search_fields = ("mahsulot__nomi", "ombor__nomi")


@admin.register(OmborChiqim)
class OmborChiqimAdmin(admin.ModelAdmin):
    list_display = ("id", "mahsulot", "ombor", "miqdor", "tasdiqlash", "sana")


@admin.register(MahsulotNarxi)
class MahsulotNarxiAdmin(admin.ModelAdmin):
    list_display = ("id", "mahsulot", "narx", "chegirma")


@admin.register(MahsulotSoni)
class MahsulotSoniAdmin(admin.ModelAdmin):
    list_display = ("id", "mahsulot", "ombor", "soni")


@admin.register(OmborKochirish)
class OmborKochirishAdmin(admin.ModelAdmin):
    list_display = ("id", "mahsulot", "hozirgi_ombor", "yangi_ombor", "miqdor", "sana")


@admin.register(Xarajat)
class XarajatAdmin(admin.ModelAdmin):
    list_display = ("id", "xarajat_turi", "summa", "kassir", "sana")
    search_fields = ("xarajat_turi",)


@admin.register(KassaKirim)
class KassaKirimAdmin(admin.ModelAdmin):
    list_display = ("id", "kirim_turi", "summa", "kassir", "sana")


@admin.register(Buyurtma)
class BuyurtmaAdmin(admin.ModelAdmin):
    list_display = ("id", "mijoz_ismi", "mijoz_telefoni", "kassir", "sana")
    search_fields = ("mijoz_ismi", "mijoz_telefoni")


@admin.register(BuyurtmaMahsulot)
class BuyurtmaMahsulotAdmin(admin.ModelAdmin):
    list_display = ("id", "buyurtma", "mahsulot", "soni", "narx")


@admin.register(Tolov)
class TolovAdmin(admin.ModelAdmin):
    list_display = ("id", "buyurtma", "shartnoma_kodi", "summa", "sana")


@admin.register(Filial)
class FilialAdmin(admin.ModelAdmin):
    list_display = ("id", "nomi")


@admin.register(NarxSozlamalari)
class NarxSozlamalariAdmin(admin.ModelAdmin):
    list_display = ("id", "filial", "mahsulot_turi", "soni", "foiz", "status")
