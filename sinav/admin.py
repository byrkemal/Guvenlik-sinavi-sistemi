from django.contrib import admin
from .models import SinavKullanicisi, Soru, Sinav, SinavSonucu

class SinavKullanicisiAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        # Şifreyi olduğu gibi kaydetsin (hashlemesin)
        obj.sifre = form.cleaned_data['sifre']
        super().save_model(request, obj, form, change)

@admin.register(SinavSonucu)
class SinavSonucuAdmin(admin.ModelAdmin):
    list_display = ('kullanici', 'dogru_sayisi', 'yanlis_sayisi', 'puan', 'tarih')
    list_filter = ('tarih',)
    search_fields = ('kullanici__kullanici_adi',)

@admin.register(Sinav)
class SinavAdmin(admin.ModelAdmin):
    list_display = ('baslik', 'sure')
    fields = ('baslik', 'sure')
    help_texts = {
        'sure': 'Sınav süresi dakika cinsinden belirtilmelidir.'
    }

admin.site.register(SinavKullanicisi, SinavKullanicisiAdmin)
admin.site.register(Soru)