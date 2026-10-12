
"""Flask application for emotion detection."""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """Analyze text and return emotion scores."""
    text = request.args.get("textToAnalyze", "")

    if not text.strip():
        return jsonify({"error": "Please enter some text"}), 400

    result = emotion_detector(text)

    if result is None:
        return jsonify({"error": "Unable to analyze the text"}), 400

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
