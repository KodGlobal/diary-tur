# İçeri aktarma
from flask import Flask, render_template,request, redirect
# Veri tabanı kütüphanesini içeri aktarma
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# SQLite'a bağlanma
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veri tabanı oluşturma
db = SQLAlchemy(app )

# Görev #1. Bir veri tabanı tablosu oluştur


# Sayfa içeriğini çalıştırma
@app.route('/')
def index():
    # DB objelerini göstermek
    # Görev #2. objeleri veri tabanından index.html'de göster 
    

    return render_template('index.html',
                           #cards = cards

                           )

# card sayfasını gösterme
@app.route('/card/<int:id>')
def card(id):
    # Görev #2. id'sine göre doğru kartı göster
    

    return render_template('card.html', card=card)

# Sayfayı çalıştırma ve kart oluşturma
@app.route('/create')
def create():
    return render_template('create_card.html')

# Kart formu
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        # Görev #2. Veri tabanında bilgiyi depolamanın bir yolunu bul!
        




        return redirect('/')
    else:
        return render_template('create_card.html')


if __name__ == "__main__":
    app.run(debug=True)
