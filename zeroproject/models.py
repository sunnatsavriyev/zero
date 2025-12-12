from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



#   MAHSULOTLAR BO‘LIMI


class MahsulotKategoriya(models.Model):
    nomi = models.CharField(max_length=255)
    izoh = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=True)  # active/inactive

    def __str__(self):
        return self.nomi


class MahsulotBrend(models.Model):
    nomi = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nomi


class Mahsulot(models.Model):
    nomi = models.CharField(max_length=255)
    kategoriya = models.ForeignKey(MahsulotKategoriya, on_delete=models.SET_NULL, null=True)
    brend = models.ForeignKey(MahsulotBrend, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)
    izoh = models.TextField(blank=True, null=True)
    rasm = models.ImageField(upload_to='mahsulotlar/', blank=True, null=True)

    def __str__(self):
        return self.nomi


class Ombor(models.Model):
    nomi = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    filial = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class YetkazibBeruvchi(models.Model):
    nomi = models.CharField(max_length=255)
    rasmiy_nomi = models.CharField(max_length=255)
    telefon = models.CharField(max_length=30)
    manzil = models.CharField(max_length=255)
    izoh = models.TextField(blank=True, null=True)
    valyuta_turi = models.CharField(max_length=10, choices=[("UZS", "UZS"), ("USD", "USD")])
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.nomi


class OmborKirim(models.Model):
    yetkazib_beruvchi = models.ForeignKey(YetkazibBeruvchi, on_delete=models.SET_NULL, null=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    miqdor = models.IntegerField()
    valyuta_turi = models.CharField(max_length=10)
    kurs = models.DecimalField(max_digits=12, decimal_places=2)
    tolov_turi = models.CharField(max_length=20)  # naqd, pul ko‘chirish
    izoh = models.TextField(blank=True, null=True)
    sana = models.DateField(auto_now_add=True)


class OmborChiqim(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    miqdor = models.IntegerField()
    tasdiqlash = models.BooleanField(default=False)
    sana = models.DateField(auto_now_add=True)


class MahsulotNarxi(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    narx = models.DecimalField(max_digits=12, decimal_places=2)
    chegirma = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    izoh = models.TextField(blank=True, null=True)


class MahsulotSoni(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)
    soni = models.IntegerField()


class OmborKochirish(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    hozirgi_ombor = models.ForeignKey(Ombor, related_name="from_ombor", on_delete=models.CASCADE)
    yangi_ombor = models.ForeignKey(Ombor, related_name="to_ombor", on_delete=models.CASCADE)
    miqdor = models.IntegerField()
    status = models.CharField(max_length=20)  # o‘xshash: o‘tgan, bekor
    sana = models.DateField(auto_now_add=True)



#   KASSA BO‘LIMI


class Xarajat(models.Model):
    xarajat_turi = models.CharField(max_length=255)
    summa = models.DecimalField(max_digits=12, decimal_places=2)
    izoh = models.TextField(blank=True, null=True)
    kassir = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    sana = models.DateField(auto_now_add=True)


class KassaKirim(models.Model):
    kirim_turi = models.CharField(max_length=255)
    summa = models.DecimalField(max_digits=12, decimal_places=2)
    izoh = models.TextField(blank=True, null=True)
    kassir = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    sana = models.DateField(auto_now_add=True)



#   BUYURTMA / SOTUV


class Buyurtma(models.Model):
    mijoz_ismi = models.CharField(max_length=255)
    mijoz_telefoni = models.CharField(max_length=30)
    sana = models.DateField(auto_now_add=True)
    kassir = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Buyurtma #{self.id}"


class BuyurtmaMahsulot(models.Model):
    buyurtma = models.ForeignKey(Buyurtma, related_name="items", on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    soni = models.IntegerField()
    narx = models.DecimalField(max_digits=12, decimal_places=2)

    def get_sum(self):
        return self.soni * self.narx


class Tolov(models.Model):
    buyurtma = models.ForeignKey(Buyurtma, on_delete=models.CASCADE)
    shartnoma_kodi = models.CharField(max_length=255)
    summa = models.DecimalField(max_digits=12, decimal_places=2)
    sana = models.DateField(auto_now_add=True)



#   NARX SOZLAMALARI


class Filial(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi


class NarxSozlamalari(models.Model):
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    mahsulot_turi = models.CharField(max_length=255)
    soni = models.IntegerField()
    foiz = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=True)
