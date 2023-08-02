# Deploy ML models with FastAPI, Docker, and Render

Inspired by:
- [render-examples/fastapi](https://github.com/render-examples/fastapi/tree/main)
- [Youtube video by AssemblyAI](https://youtu.be/h5wLuVDr0oc)

## How to deploy

### 1. Develop and save the model with this Colab

[Open Colab](https://colab.research.google.com/drive/1uaALcaatvxOu42IhQA4r0bahfdpw-Z7v?usp=sharing)

### 2. Deploy in render

- Specify the URL to your new repository or this repository.

- Render will automatically detect that you are deploying a Python qervice and use pip to download the dependencies.

- Specify the following as the Start Command.
```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

- Click Create Web Service.


## How to test it

### Using CURL

```bash
curl -X 'POST' \
  'https://assemblyai-project.onrender.com/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Hola, ¿cómo estás?"
}'
```

Answer should be something like:

```bash
{
    "language": "Spanish"
}
```

### Using httpie

- First install the python package
```bash
pip install httpie
```

- Then run this command with your preferred text:

```bash
https -v GET assemblyai-project.onrender.com
```

Answer should be something like:

```bash
{
    "health_check": "OK",
    "model_version": "0.1.0"
}
```

- Try with this one

```bash
https -v POST assemblyai-project.onrender.com/predict text="Comment allez-vous?"
```

Answer should be something like:

```bash
{
    "language": "French"
}
```
