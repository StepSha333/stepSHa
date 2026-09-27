from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return {"status": "ok", "service": "devops-portfolio-app"}

@app.get("/health")
def health():
    return {"health": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
