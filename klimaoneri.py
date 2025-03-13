import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Girdi ve Çıktı Değişkenlerini Tanımla
dis_sicaklik = ctrl.Antecedent(np.arange(-10, 50, 1), 'dis_sicaklik')
kisi_sayisi = ctrl.Antecedent(np.arange(0, 20, 1), 'kisi_sayisi')
klima_sicakligi = ctrl.Consequent(np.arange(16, 30, 1), 'klima_sicakligi')

# Üyelik Fonksiyonlarını Tanımla
dis_sicaklik['dusuk'] = fuzz.trimf(dis_sicaklik.universe, [-10, 0, 20])
dis_sicaklik['orta'] = fuzz.trimf(dis_sicaklik.universe, [10, 20, 30])
dis_sicaklik['yuksek'] = fuzz.trimf(dis_sicaklik.universe, [25, 35, 50])

kisi_sayisi['az'] = fuzz.trimf(kisi_sayisi.universe, [0, 0, 5])
kisi_sayisi['orta'] = fuzz.trimf(kisi_sayisi.universe, [3, 7, 12])
kisi_sayisi['cok'] = fuzz.trimf(kisi_sayisi.universe, [10, 15, 20])

klima_sicakligi['dusuk'] = fuzz.trimf(klima_sicakligi.universe, [16, 18, 22])
klima_sicakligi['orta'] = fuzz.trimf(klima_sicakligi.universe, [20, 22, 26])
klima_sicakligi['yuksek'] = fuzz.trimf(klima_sicakligi.universe, [24, 26, 30])

# Kuralları Tanımla
kural1 = ctrl.Rule(dis_sicaklik['dusuk'] & kisi_sayisi['az'], klima_sicakligi['yuksek'])
kural2 = ctrl.Rule(dis_sicaklik['dusuk'] & kisi_sayisi['orta'], klima_sicakligi['orta'])
kural3 = ctrl.Rule(dis_sicaklik['dusuk'] & kisi_sayisi['cok'], klima_sicakligi['dusuk'])
kural4 = ctrl.Rule(dis_sicaklik['orta'] & kisi_sayisi['az'], klima_sicakligi['orta'])
kural5 = ctrl.Rule(dis_sicaklik['orta'] & kisi_sayisi['orta'], klima_sicakligi['orta'])
kural6 = ctrl.Rule(dis_sicaklik['orta'] & kisi_sayisi['cok'], klima_sicakligi['dusuk'])
kural7 = ctrl.Rule(dis_sicaklik['yuksek'] & kisi_sayisi['az'], klima_sicakligi['dusuk'])
kural8 = ctrl.Rule(dis_sicaklik['yuksek'] & kisi_sayisi['orta'], klima_sicakligi['dusuk'])
kural9 = ctrl.Rule(dis_sicaklik['yuksek'] & kisi_sayisi['cok'], klima_sicakligi['dusuk'])

# Kontrol Sistemi ve Simülasyon
sicaklik_kontrol = ctrl.ControlSystem([kural1, kural2, kural3, kural4, kural5, kural6, kural7, kural8, kural9])
model_sicaklik = ctrl.ControlSystemSimulation(sicaklik_kontrol)

# Girdi Değerlerini Ayarla
model_sicaklik.input['dis_sicaklik'] = 20
model_sicaklik.input['kisi_sayisi'] = 4

# Hesaplama Yap
model_sicaklik.compute()

# Sonucu Yazdır
print(f"Önerilen Klima Sıcaklığı: {model_sicaklik.output['klima_sicakligi']:.2f}°C")