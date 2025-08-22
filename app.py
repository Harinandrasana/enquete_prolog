from flask import Flask, render_template, request
from pyswip import Prolog
import os

app = Flask(__name__)

class CrimeDetectionEngine:
    def __init__(self):
        self.prolog = Prolog()
        self.load_prolog_file()

    def load_prolog_file(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        prolog_file = os.path.join(current_dir, "crime.pl")
        if os.path.exists(prolog_file):
            self.prolog.consult(prolog_file)
        else:
            print("Fichier crime.pl non trouvé")

    def get_suspects(self):
        return sorted(set(res['X'] for res in self.prolog.query('suspect(X)')))

    def get_crime_types(self):
        return sorted(set(res['X'] for res in self.prolog.query('crime_type(X)')))

    def check_guilt(self, suspect, crime_type):
        query = f"is_guilty({suspect}, {crime_type})"
        return bool(list(self.prolog.query(query)))

engine = CrimeDetectionEngine()

@app.route('/', methods=['GET'])
def index():
    suspects = engine.get_suspects()
    crimes = engine.get_crime_types()
    return render_template('index.html', suspects=suspects, crime_types=crimes, result=None)

@app.route('/analyze', methods=['POST'])
def analyze():
    suspect = request.form.get('suspect')
    crime_type = request.form.get('crime_type')
    if not suspect or not crime_type:
        result = "Veuillez sélectionner un suspect et un type de crime."
    else:
        guilty = engine.check_guilt(suspect, crime_type)
        result = "COUPABLE" if guilty else "NON COUPABLE"
    suspects = engine.get_suspects()
    crimes = engine.get_crime_types()
    return render_template('index.html',
                           suspects=suspects,
                           crime_types=crimes,
                           suspect=suspect,
                           crime_type=crime_type,
                           result=result)

if __name__ == '__main__':
    app.run(debug=True)
