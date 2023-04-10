from flask import Flask, render_template, url_for, request, session, redirect, abort

app = Flask(__name__)

app.config['SECRET_KEY'] = '65fc74dc8f453b48af092bb103344f88aca00260'  # os.urandom(20).hex()
#  session.permanent=False
#  app.permanent_session_lifetime(days=3)
#  session.modified = True
menu = ["Список опрошенных", "Результаты", "Описания"]


@app.route("/")
def index():
    print(url_for('index'))
    return render_template("index.html", menu=menu)


@app.route("/result")
def result():
    print(url_for('result'))
    return render_template("result.html", title="Результаты")


@app.route("/form", methods=["POST", "GET"])
def form():
    if request.method == "POST":
        print(request.form)

    return render_template("form.html", title='Форма', menu=menu)


@app.errorhandler(404)
def pageNotFount(error):
    return render_template("page404.html", title="Страница не найдена", menu=menu), 404


@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "nevasv" and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=menu)


#
# @app.route("/profile", methods=["POST", "GET"])
# def profile(username):
#     return f"Профиль пользователя {username}"
#

@app.route("/profile/<username>", methods=["POST", "GET"])
def profile(username):
    if 'userlogged' not in session or session['userLogged'] != 'username':
        abort(401)
        return f"Профиль пользователя {username}"


if __name__ == "__main__":
    app.run(debug=True)
