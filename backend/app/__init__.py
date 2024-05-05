import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .database import db
from .controllers.blog_controller import blog_blueprint
from .controllers.ingredient_controller import ingredient_blueprint
# import subprocess  # Alt islem (subprocess) modulu
# import time

# def run_populate_databases():
#     # Dosya yolunu düzeltin
#     file_path = "C:/Users/celik/Desktop/yazilimmuh/facefact/backend/data_processing/populate_databases.py"
#     # Python dosyasýný çalýþtýrmak için subprocess kullanýn
#     subprocess.run(["python", file_path], check=True)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'  # Guvenlik anahtarini belirleyin

    # .env dosyasini yukle
    load_dotenv()

    # .env dosyasindan yapilandirma ayarlarini al
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///default.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    
    # Veritaban
    # 
    # 
    # i baglantisini baslat
    db.init_app(app)

    # Blueprintleri kaydet
    app.register_blueprint(blog_blueprint, url_prefix='/')
    app.register_blueprint(ingredient_blueprint, url_prefix='/')

    # Ýstege bagli olarak CORS destegini etkinlestirin
    CORS(app, supports_credentials=True)

    # Veritabani tablolarini olustur
    with app.app_context():
        db.create_all()  # Tablolari olusturmak icin
        # run_populate_databases()
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
