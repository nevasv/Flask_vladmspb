from flask import Flask, render_template, url_for, request

app = Flask(__name__)

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


if __name__ == "__main__":
    app.run(debug=True)
