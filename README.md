# ❄️ FuzzyClimateControl  
**Dış sıcaklık ve kişi sayısına göre klima sıcaklığını optimize eden bulanık mantık tabanlı kontrol sistemi**  

## 🚀 Özellikler  
- Dış sıcaklık ve kişi sayısını giriş olarak kullanır.  
- Bulanık mantık kuralları ile klima sıcaklığını dinamik olarak belirler.  
- Esnek ve özelleştirilebilir üyelik fonksiyonları içerir.  
- Çevresel faktörlere duyarlı akıllı klima kontrolü sağlar.  

## 🛠️ Kullanılan Teknolojiler  
- **Python**  
- **NumPy**  
- **scikit-fuzzy**  

## 📌 Nasıl Çalışır?  

### **Girdi Değişkenleri:**  
- `dis_sicaklik`: Dış ortam sıcaklığı (-10°C ile 50°C arasında)  
- `kisi_sayisi`: Odadaki kişi sayısı (0-20 kişi)  

### **Çıktı Değişkeni:**  
- `klima_sicakligi`: Önerilen klima sıcaklığı (16°C - 30°C)  

### **Bulanık Mantık Kuralları:**  
- Hava **soğuk** ve kişi sayısı **az** ise, klima sıcaklığı **yüksek** olmalı.  
- Hava **sıcak** ve kişi sayısı **çok** ise, klima sıcaklığı **düşük** olmalı.  
- **Orta seviyelerde** uygun bir sıcaklık belirlenir.  

## 💻 Örnek Çalıştırma  

Aşağıdaki girişler için önerilen klima sıcaklığı hesaplanır:  

```python
model_sicaklik.input['dis_sicaklik'] = 20
model_sicaklik.input['kisi_sayisi'] = 4
model_sicaklik.compute()
print(f"Önerilen Klima Sıcaklığı: {model_sicaklik.output['klima_sicakligi']:.2f}°C")
```

