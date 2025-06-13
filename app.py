from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Načtení API klíče z proměnné prostředí
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "Jaké je hlavní město Francie?")

        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        answer = completion.choices[0].message.content.strip()
        return jsonify({"response": answer})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Důležité pro Render: běž na portu z proměnné prostředí
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
