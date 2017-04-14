from flask import Flask, request, render_template
from diceware import generate_diceware_pw

app = Flask(__name__)

@app.route('/')
def show_homepage():
    """Display homepage where user can generate diceware passwords."""

    return render_template('index.html')


@app.route('/generate-diceware', methods=['POST'])
def generate_diceware():
    """Generate diceware password using length inputted by user."""

    word_count = request.form.get('pw-length')

    diceware_pw = generate_diceware_pw(word_count)

    return render_template('generate_diceware.html', diceware_pw=diceware_pw)


if __name__ == "__main__":
    app.run(debug=True)
