from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
# Mahsulotlar
router.register(r"kategoriya",MahsulotKategoriyaViewSet, basename="kategoriya")
router.register(r"brend",MahsulotBrendViewSet, basename="brend")
router.register(r"mahsulot", MahsulotViewSet, basename="mahsulot")

# Ombor
router.register(r"ombor",OmborViewSet, basename="ombor")
router.register(r"yetkazib",YetkazibBeruvchiViewSet, basename="yetkazib")
router.register(r"ombor-kirim",OmborKirimViewSet, basename="ombor-kirim")
router.register(r"ombor-chiqim",OmborChiqimViewSet, basename="ombor-chiqim")
router.register(r"ombor-kochirish",OmborKochirishViewSet, basename="ombor-kochirish")
router.register(r"mahsulot-narxi",MahsulotNarxiViewSet, basename="mahsulot-narxi")
router.register(r"mahsulot-soni",MahsulotSoniViewSet, basename="mahsulot-soni")

# Kassa
router.register(r"xarajat", XarajatViewSet, basename="xarajat")
router.register(r"kirim", KassaKirimViewSet, basename="kirim")

# Buyurtma / Tolov
router.register(r"buyurtma", BuyurtmaViewSet, basename="buyurtma")
router.register(r"buyurtma-item", BuyurtmaMahsulotViewSet, basename="buyurtma-item")
router.register(r"tolov", TolovViewSet, basename="tolov")

# Filial / narx sozlamalari
router.register(r"filial", FilialViewSet, basename="filial")
router.register(r"narx-sozlama", NarxSozlamalariViewSet, basename="narx-sozlama")

urlpatterns = [
    path("", include(router.urls)),
]
