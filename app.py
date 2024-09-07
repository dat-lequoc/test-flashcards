from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# In-memory storage for flashcards
flashcards = []

@app.route('/api/flashcards', methods=['GET', 'POST'])
def handle_flashcards():
    if request.method == 'GET':
        return jsonify(flashcards)
    elif request.method == 'POST':
        new_flashcard = request.json
        flashcards.append(new_flashcard)
        return jsonify(new_flashcard), 201

@app.route('/api/flashcards/clear', methods=['POST'])
def clear_flashcards():
    global flashcards
    flashcards = []
    return '', 204

@app.route('/api/generate', methods=['POST'])
def generate_content():
    data = request.json
    selected_text = data.get('selectedText', '')
    mode = data.get('mode', 'flashcard')
    
    # Simulate AI-generated content (replace with actual AI integration)
    if mode == 'flashcard':
        generated_content = {
            'question': f"Question about: {selected_text[:30]}...",
            'answer': f"Answer related to: {selected_text[:30]}..."
        }
    elif mode == 'explain':
        generated_content = {
            'explanation': f"Explanation of: {selected_text[:30]}..."
        }
    elif mode == 'language':
        generated_content = {
            'translation': f"Translation of: {selected_text[:30]}..."
        }
    else:
        return jsonify({'error': 'Invalid mode'}), 400

    return jsonify(generated_content)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
