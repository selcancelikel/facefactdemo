
from flask import Blueprint, jsonify, request, render_template




from .. import db  
# from ..models import Ingredient
from ..models import Blog
from ..models import Ingredient

ingredient_blueprint = Blueprint("ingredient_blueprint", __name__)



@ingredient_blueprint.route("/ingredient", methods=["POST"])
def denemem():
    try:
        data = request.get_json()
    except:
        return jsonify({"message": "Invalid data"}), 400

    try:
        new_ingredient = Ingredient(name=data["name"], isHarmful=data["isHarmful"], harmfulSkin=data["harmfulSkin"])
        db.session.add(new_ingredient)
        db.session.commit()
        return jsonify(new_ingredient.json()), 201
    except:
        return jsonify({"message": "An error occurred creating the ingredient"}), 500










@ingredient_blueprint.route("/data", methods=["GET"])
def create_ingredient():
    try:
        data = {
    "name": "Ingredient2",
    "isHarmful": True,
}
    except:
        return jsonify({"message": "Invalid data"}), 400

    try:
        new_ingredient = Ingredient(name=data["name"],isHarmful=data["isHarmful"])
        db.session.add(new_ingredient)
        db.session.commit()
        return "basarili kaydedildi"
        
    except:
        return "hata"
            


@ingredient_blueprint.route("/compare", methods=["POST"])
def compare():
   
    skin_types = ["yagli cilt", "kuru cilt", "karma cilt"]

    # Veritabanindaki tum icerikleri alin
    all_ingredients_in_db = Ingredient.query.all()
    harmful_ingredients = []  # Zararli icerikleri saklamak icin liste
    pore_clogging_ingredients = []  # Gozenek tikayici icerikleri saklamak icin liste

    try:
        # Form verilerini al
        # skin_type = request.form.get("radiobutton", "").strip().lower()
        ingredients = request.form.get("ingredient", "").strip()
        skin_type = request.form.get('radiobutton')
        
        # Eger form verilerinden bir veri eksikse veya gecersizse hata donun
        if not skin_type or not ingredients:
            return jsonify({"message": "Eksik veya gecersiz veri"}), 400

        # Cilt tipinin gecerli olup olmadigini kontrol edin
        if skin_type not in skin_types:
            return jsonify({"message": "gecersiz cilt tipi"}), 400

        # Ingredients'i virgul ile ayirarak listeye cevirin
        ingredients_list = [ingredient.strip().lower() for ingredient in ingredients.split(",")]

        # Veritabanindaki icerikleri kontrol ederek zararli ve gozenek tikayici icerikleri belirleyin
        for ingredient in ingredients_list:
            for db_ingredient in all_ingredients_in_db:
                if db_ingredient.name.lower() == ingredient:
                    if db_ingredient.isHarmful and skin_type in db_ingredient.harmfulSkin.lower():
                        harmful_ingredients.append(db_ingredient.name)
                    if db_ingredient.isHarmful and "gozenek tikayici" in db_ingredient.harmfulSkin.lower():
                        pore_clogging_ingredients.append(db_ingredient.name)

        # Zararli ve gozenek tikayici icerikler icin mesajlari olusturun
        harmful_ingredients_message = f"Sectiginiz cilt tipi '{skin_type}' icin zararli olan icerikler: "
        harmful_ingredients_message += ", ".join(harmful_ingredients) if harmful_ingredients else "Bulunmamaktadir."

        pore_clogging_ingredients_message = f"Sectiginiz cilt tipi '{skin_type}' icin gozenek tikayici olan icerikler: "
        pore_clogging_ingredients_message += ", ".join(pore_clogging_ingredients) if pore_clogging_ingredients else "Bulunmamaktadir."

        # JSON yanitini donun
        return jsonify({"harmfulIngredients": harmful_ingredients_message, "poreCloggingIngredients": pore_clogging_ingredients_message}), 200

    except Exception as e:
        # Hatayi loglamak icin bir logger veya print kullanabilirsiniz
        print(f"Bir hata olustu: {e}")
        return jsonify({"message": "Bir hata olustu"}), 500

# @ingredient_blueprint.route("/ingredient/compare", methods=["POST"])
# def compare_ingredients():
#     """
#     Input:
#         skinType: string
#         ingredients: list of strings (comma separated)
#     Output:
#         list of ingredients that are harmful to the skinType
#     """
#     skin_types = ["yagli cilt", "kuru cilt", "karma cilt"]

#     all_ingredients_in_db = Ingredient.query.all()
#     harmful_ingredients = []  # list of harmful ingredients for the skin type
#     pore_clogging_ingredients = []  # list of pore-clogging ingredients for the skin type
#     try:
#         data = request.get_json()
#         skin_type = data["skinType"]
#         ingredients = data["ingredients"]
#         ingredients = [ingredient.strip() for ingredient in ingredients.split(",")]
#         if skin_type.lower() not in skin_types:
#             return jsonify({"message": "Invalid skin type"}), 400
#         for ingredient in ingredients:
#             for db_ingredient in all_ingredients_in_db:
#                 if db_ingredient.name.lower() == ingredient.lower():
#                     if db_ingredient.isHarmful and skin_type.lower() in db_ingredient.harmfulSkin.lower():
#                         harmful_ingredients.append(db_ingredient.name)
#                     elif db_ingredient.isHarmful and "pore clogging" in db_ingredient.harmfulSkin.lower():
#                         pore_clogging_ingredients.append(db_ingredient.name)

#         harmful_ingredients_message = f"Ingredients harmful to the selected skin type '{skin_type}': "
#         for ingredient in harmful_ingredients:
#             harmful_ingredients_message += ingredient + ", "
#         if len(harmful_ingredients) == 0:
#             harmful_ingredients_message += "None."
#         pore_clogging_ingredients_message = f"Ingredients pore-clogging to the selected skin type '{skin_type}': "
#         for ingredient in pore_clogging_ingredients:
#             pore_clogging_ingredients_message += ingredient + ", "
#         if len(pore_clogging_ingredients) == 0:
#             pore_clogging_ingredients_message += "None."
#         return jsonify({"harmfulIngredients": harmful_ingredients_message, "poreCloggingIngredients": pore_clogging_ingredients_message}), 200
#     except:
#         return jsonify({"message": "Invalid data"}), 400
