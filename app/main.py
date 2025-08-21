from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/add", methods=["GET"])
def add():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a + b}), 200
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(debug=True)

