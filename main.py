import random

from flask import Flask, render_template, request

app = Flask(__name__)

PREDICTIONS = [
    "Сегодня отличный день для чашки крепкого эспрессо!",
    "Кофе с молоком принесет удачу в делах.",
    "Не пей кофе на ночь, иначе будешь считать овец до утра.",
    "Добавь корицу в кофе — и день сложится удачно!",
    "Твой идеальный напиток сегодня — латте с карамелью.",
    "Осторожно: сегодня вы рискуете влюбиться в капучино.",
    "Утренний кофе спасет мир. Начни с себя.",
    "Если сомневаешься, что выбрать — бери двойной эспрессо.",
    "Сегодня твой кофе будет особенно вкусным. Наслаждайся!",
    "Не забудь сделать глоток кофе перед важным разговором.",
    "Зерна для твоего напитка сегодня выбраны удачно.",
    "Твоя энергия сегодня на 100% зависит от первой чашки.",
    "Делись кофе с друзьями — вернется вдвойне.",
    "Сегодня идеальный день, чтобы попробовать новый сорт.",
    "Пусть пенка на твоем кофе будет такой же легкой, как твои проблемы."
]

@app.route("/", methods=["GET", "POST"])
def index():
    
    prediction = None
    if request.method == "POST":
        prediction = random.choice(PREDICTIONS)
        
    return render_template("index.html", prediction=prediction)


@app.route("/blog")
def blog():
    """
         Отрисовка страницы блога 
         
     """
    return render_template("blog.html")

@app.route("/blog/1")
def blog1():
     """
    Отрисовка страницы блога №1
             
    """
     return render_template("post_espresso.html")

@app.route("/post")
def post():
     
   return render_template("example.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog/cappuccino")
def post_cappuccino():
    return render_template("post_cappuccino.html")

@app.route("/blog/latte")
def post_latte():
    return render_template("post_latte.html")
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)