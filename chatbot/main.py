from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Configura tu clave de API de OpenAI
OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input', '')
    response_text = generate_response(user_input)
    return jsonify({'response': response_text})

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50  # Ajusta esto según tus necesidades
    )
    return response.choices[0].text.strip()

if __name__ == '__main__':
    app.run(debug=True)

