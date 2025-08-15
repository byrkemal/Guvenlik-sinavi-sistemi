from django.db import models
import os
class Soru(models.Model):
    gorsel = models.ImageField(upload_to='gorseller/')
    
    def __str__(self):
        # Görselin dosya yolunu al ve dosya adını çıkar
        gorsel_adi = os.path.basename(self.gorsel.name).split('.')[0]  # Yalnızca dosya adını al
        gorsel_adi = gorsel_adi.replace('_', ' ')  # "_" yerine boşluk koy
        return gorsel_adi


class SinavKullanicisi(models.Model):
    kullanici_adi = models.CharField(max_length=50, unique=True)
    sifre = models.CharField(max_length=50)
    sinava_girdi_mi = models.BooleanField(default=False)

    def __str__(self):
        return self.kullanici_adi

class Sinav(models.Model):
    baslik = models.CharField(max_length=100, default="Güvenlik Sınavı")
    sure = models.IntegerField(help_text="Sınav süresi (dakika cinsinden)")

    def __str__(self):
        return f"{self.baslik} - {self.sure} dakika"    
    

class SinavSonucu(models.Model):
    kullanici = models.ForeignKey('SinavKullanicisi', on_delete=models.CASCADE)
    dogru_sayisi = models.IntegerField()
    yanlis_sayisi = models.IntegerField()
    puan = models.IntegerField()
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.kullanici.kullanici_adi} - {self.puan} Puan"    