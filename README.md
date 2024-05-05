# facefactdemo
1-)terminal üzerinden projenin ana dizinine gelin

2-)env yapılandırması için:
python -m venv myenv

3-)env aktif etmek için
myenv\Scripts\activate
bu işlemlerden sonra projeninizin ana dizininde myenv dosyası oluşacak kontrol edi

4-)backend dizinine gelin(requirements
cd backend

5-)Gerekli kütüphanelerin indirilmesi
pip install -r requirements.txt

6-)projenin run edilmesi
python run.py

projenizi browserdan http://127.0.0.1:5000/anasayfa yazarak ulaşabilirsiniz.

ek olarak
databasei doldurmak için terminali kapatmadan yeni bir terminal daha açın ardından projedeki data_processing dizinine gelin
python populate_databases.py
komutunu giriniz.
artık sitedeki textarea kısmına ürünleri girerek deneyebilirsiniz

