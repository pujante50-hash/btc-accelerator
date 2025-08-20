from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    txid = request.form['txid']
    # Aquí irá la lógica de verificación y aceleración
    return f"TXID recibido: {txid}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)