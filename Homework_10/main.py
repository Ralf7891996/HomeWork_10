# Импортируем библиотеки и функции
from utils import get_all, get_by_pk, get_by_skill
from flask import Flask

app = Flask(__name__)


# создаем представление для роута
@app.route("/")
def index():
    candidates = get_all()
    result = '<br>'
    for candidate in candidates:
        result += 'Имя кандидата: ' + candidate['name'] + '</br>'
        result += 'Позиция кандидата: ' + candidate['position'] + '</br>'
        result += 'Навыки: ' + candidate['skills'] + '</br>'
        result += '<br>'

    return f'<pre> {result} </pre>'


# создаем представление для роута, показывающее кандидата по pk
@app.route("/candidates/<int:pk>")
def get_candidate_by_pk(pk):
    candidate = get_by_pk(pk)
    if candidate == "Mistake": #Если кандидата с таким pk не существут, указывает ошибку
        return "Mistake"
    else:
        result = '<br>'
        result += 'Имя кандидата: ' + candidate['name'] + '</br>'
        result += 'Позиция кандидата: ' + candidate['position'] + '</br>'
        result += 'Навыки: ' + candidate['skills'] + '</br>'
        result += '<br>'
        return f"""
               <img src="{candidate['picture']}">
               <pre> {result} </pre>
               """


# создаем представление для роута, показывающее кандидата по навыкам
@app.route("/skills/<skill>")
def get_candidate_by_skill(skill):
    candidates = get_by_skill(skill)
    result = '<br>'
    for candidate in candidates:
        result += 'Имя кандидата: ' + candidate['name'] + '</br>'
        result += 'Позиция кандидата: ' + candidate['position'] + '</br>'
        result += 'Навыки: ' + candidate['skills'] + '</br>'
        result += '<br>'
    return f'<pre> {result} </pre>'


app.run(debug=True, host='0.0.0.0', port=800)
