from flask import Flask, jsonify, request

app = Flask(__name__)

courses = [
    {
        'id': 1,
        'title': 'Curso de Python',
        'description': 'Aprenda programação em Python',
        'carga_horaria': 40,
        'qtd_exercicios': 10
    },
    {
        'id': 2,
        'title': 'Curso de Web Development',
        'description': 'Aprenda a criar sites e aplicações web',
        'carga_horaria': 60,
        'qtd_exercicios': 15
    },
    {
        'id': 3,
        'title': 'Curso de Data Science',
        'description': 'Aprenda análise de dados e machine learning',
        'carga_horaria': 80,
        'qtd_exercicios': 20
    },
    {
        'id': 4,
        'title': 'Curso de Desenvolvimento Mobile',
        'description': 'Aprenda a criar aplicativos para dispositivos móveis',
        'carga_horaria': 50,
        'qtd_exercicios': 12
    },
    {
        'id': 5,
        'title': 'Curso de Inteligência Artificial',
        'description': 'Explore os fundamentos da inteligência artificial',
        'carga_horaria': 70,
        'qtd_exercicios': 18
    },
    {
        'id': 6,
        'title': 'Curso de Segurança Cibernética',
        'description': 'Aprenda a proteger sistemas e redes contra ameaças cibernéticas',
        'carga_horaria': 55,
        'qtd_exercicios': 14
    }
]

@app.route('/courses', methods=['GET'])
def get_all_courses():
    return jsonify(courses)



if __name__ == '__main__':
    app.run(debug=True)
