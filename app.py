from flask import Flask, render_template, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the GPT-2 model
generator = pipeline("text-generation", model="gpt2")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate-quote")
def generate_quote():
    prompt = "Motivational quote: "
    result = generator(prompt, max_length=50, num_return_sequences=1, do_sample=True, temperature=0.9)
    quote = result[0]["generated_text"].split("\n")[0]  # Get the first line
    return jsonify({"quote": quote.strip()})

if __name__ == "__main__":
    app.run(debug=True)
