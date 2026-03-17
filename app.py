from flask import Flask, request, jsonify, render_template
from ai_engine import extract_text, generate_plan, mentor_chat

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    role = request.form["role"]
    file = request.files["resume"]

    text = extract_text(file)
    plan = generate_plan(role, text)

    return jsonify({"plan": plan})

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["msg"]
    reply = mentor_chat(msg)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
