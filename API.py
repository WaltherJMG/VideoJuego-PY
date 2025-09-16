import requests
from deep_translator import GoogleTranslator

# URL de la API
url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    for i, question in enumerate(data['results'], 1):
        # Traducir pregunta y respuestas
        pregunta_es = GoogleTranslator(source='auto', target='es').translate(question['question'])
        correct_es = GoogleTranslator(source='auto', target='es').translate(question['correct_answer'])
        incorrect_es = [GoogleTranslator(source='auto', target='es').translate(ans) for ans in question['incorrect_answers']]

        respuestas = incorrect_es + [correct_es]

        print(f"Pregunta {i}: {pregunta_es}")
        print("Opciones:")
        for j, answer in enumerate(respuestas, 1):
            print(f"  {j}. {answer}")
        print(f"Respuesta correcta: {correct_es}")
        print("-" * 40)
else:
    print("Error al obtener las preguntas:", response.status_code)
