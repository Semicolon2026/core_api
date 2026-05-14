from flask import Flask, jsonify
import onnx

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "ok",
        "service": "core_api",
        "onnx_version": onnx.__version__
    })

@app.route("/")
def home():
    return jsonify({
        "message": "core_api running"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
