from .models import Soru
import random
import os
from .models import SinavKullanicisi,SinavSonucu, Sinav
from django.shortcuts import render, redirect
from datetime import datetime, timedelta

def giris_yap(request):
    mesaj = ""
    if request.method == "POST":
        kullanici_adi = request.POST.get('kullanici_adi')
        sifre = request.POST.get('sifre')

        print("Kullanıcıdan gelen:", kullanici_adi, sifre)
        
        try:
            kullanici = SinavKullanicisi.objects.get(kullanici_adi=kullanici_adi, sifre=sifre)
            if kullanici.sinava_girdi_mi:
                mesaj = "Bu kullanıcı sınava daha önce katıldı."
            else:
                request.session['kullanici_id'] = kullanici.id
                return redirect('sinav')
        except SinavKullanicisi.DoesNotExist:
            mesaj = "Kullanıcı adı veya şifre yanlış."

    # Aktif sınavı al
    try:
        sinav = Sinav.objects.first()
        sinav_suresi = sinav.sure if sinav else 30  # Varsayılan 30 dakika
    except:
        sinav_suresi = 30

    return render(request, 'sinav/giris.html', {
        'mesaj': mesaj,
        'sinav_suresi': sinav_suresi
    })



def temizle_gorsel_adi(gorsel_adi):
    dosya_adi = os.path.basename(gorsel_adi).split('.')[0]
    parcalar = dosya_adi.split('_')[:-1]
    isim = ' '.join(parcalar)

    # Yasaklı Madde ve Tehdit Unsuru ifadelerini birleştiriyoruz
    if "Yasaklı Madde" in isim or "Tehdit Unsuru" in isim:
        return "Tehdit Unsuru Yoktur"
    return isim

def sinav_view(request):
    if 'kullanici_id' not in request.session:
        return redirect('giris')

    if 'soru_listesi' not in request.session:
        tum_sorular = list(Soru.objects.all())
        random.shuffle(tum_sorular)
        request.session['soru_listesi'] = [s.id for s in tum_sorular[:20]]
        request.session['cevaplar'] = []
        request.session['soru_index'] = 0
        
        # Sınav süresini başlat
        try:
            sinav = Sinav.objects.first()
            sinav_suresi = sinav.sure if sinav else 30
        except:
            sinav_suresi = 30
            
        request.session['sinav_baslangic'] = datetime.now().isoformat()
        request.session['sinav_suresi'] = sinav_suresi

    # Sınav süresini kontrol et
    if 'sinav_baslangic' in request.session:
        baslangic = datetime.fromisoformat(request.session['sinav_baslangic'])
        gecen_sure = datetime.now() - baslangic
        kalan_sure = timedelta(minutes=request.session['sinav_suresi']) - gecen_sure
        
        if kalan_sure.total_seconds() <= 0:
            return redirect('sinav_sonuc')

    soru_index = request.session['soru_index']
    soru_ids = request.session['soru_listesi']

    if soru_index >= len(soru_ids):
        return redirect('sinav_sonuc')

    soru = Soru.objects.get(id=soru_ids[soru_index])

    if request.method == 'POST':
        secim = request.POST.get('secim', '')  # Boş cevap için varsayılan değer
        dogru_cevap = temizle_gorsel_adi(soru.gorsel.name)

        # Seçilen cevaptan harfi kaldır
        secim = secim.split(') ')[-1] if secim and ') ' in secim else secim

        cevaplar = request.session.get('cevaplar', [])
        cevaplar.append({
            'soru_id': soru.id,
            'secilen': secim,
            'dogru': dogru_cevap
        })
        request.session['cevaplar'] = cevaplar
        request.session['soru_index'] += 1

        return redirect('sinav')

    dogru_cevap = temizle_gorsel_adi(soru.gorsel.name)

    diger_siklar = []
    for s in Soru.objects.exclude(id=soru.id):
        temiz_adi = temizle_gorsel_adi(s.gorsel.name)
        if temiz_adi != dogru_cevap and temiz_adi not in diger_siklar:
            diger_siklar.append(temiz_adi)

    if len(diger_siklar) >= 4:
        yanlis_siklar = random.sample(diger_siklar, 4)
    else:
        yanlis_siklar = diger_siklar

    tum_siklar = yanlis_siklar + [dogru_cevap]
    random.shuffle(tum_siklar)

    # Şıklara harf ekleyelim
    harfler = ['A', 'B', 'C', 'D', 'E']
    harfli_siklar = []
    for index, sik in enumerate(tum_siklar):
        harfli_siklar.append(f"{harfler[index]}) {sik}")

    # Kalan süreyi hesapla
    baslangic = datetime.fromisoformat(request.session['sinav_baslangic'])
    gecen_sure = datetime.now() - baslangic
    kalan_sure = timedelta(minutes=request.session['sinav_suresi']) - gecen_sure
    kalan_dakika = int(kalan_sure.total_seconds() // 60)
    kalan_saniye = int(kalan_sure.total_seconds() % 60)

    context = {
        'gorsel_url': soru.gorsel.url,
        'siklar': harfli_siklar,
        'soru_numarasi': soru_index + 1,
        'toplam_soru': len(soru_ids),
        'kalan_dakika': kalan_dakika,
        'kalan_saniye': kalan_saniye,
    }

    kullanici_id = request.session.get('kullanici_id')
    if kullanici_id:
        kullanici = SinavKullanicisi.objects.get(id=kullanici_id)
        kullanici.sinava_girdi_mi = True
        kullanici.save()

    return render(request, 'sinav/soru.html', context)



def sinav_sonuc(request):
    cevaplar = request.session.get('cevaplar', [])
    dogru_sayisi = sum(1 for c in cevaplar if c['secilen'] and c['secilen'] == c['dogru'])
    yanlis_sayisi = sum(1 for c in cevaplar if c['secilen'] and c['secilen'] != c['dogru'])
    bos_sayisi = sum(1 for c in cevaplar if not c['secilen'])

    # Her doğru için 5 puan verelim
    puan = dogru_sayisi * 5

    detaylar = []
    for c in cevaplar:
        try:
            soru = Soru.objects.get(id=c['soru_id'])
            gorsel_url = soru.gorsel.url
        except Soru.DoesNotExist:
            gorsel_url = ""
        detaylar.append({
            'gorsel_url': gorsel_url,
            'secilen': c['secilen'] if c['secilen'] else 'Boş Bırakıldı',
            'dogru': c['dogru'],
            'dogru_mu': c['secilen'] == c['dogru'] if c['secilen'] else False
        })
    
    # Kullanıcı bilgisi
    kullanici_id = request.session.get('kullanici_id')
    if kullanici_id:
        kullanici = SinavKullanicisi.objects.get(id=kullanici_id)

        # Veritabanına sonucu kaydet
        SinavSonucu.objects.create(
            kullanici=kullanici,
            dogru_sayisi=dogru_sayisi,
            yanlis_sayisi=yanlis_sayisi,
            puan=puan
        )
    
    # Session temizle
    request.session.flush()

    return render(request, 'sinav/sonuc.html', {
        'dogru': dogru_sayisi,
        'yanlis': yanlis_sayisi,
        'bos': bos_sayisi,
        'puan': puan,
        'detaylar': detaylar
    })


def admin_sonuc_listesi(request):
    if not request.session.get('admin_girisi'):  # Admin kontrolü yapabilirsin
        return redirect('giris')  # veya özel admin giriş
    sonuclar = SinavSonucu.objects.select_related('kullanici').order_by('-tarih')
    return render(request, 'sinav/admin_sonuclar.html', {'sonuclar': sonuclar})
