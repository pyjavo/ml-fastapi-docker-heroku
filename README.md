# Deploy ML models with FastAPI, Docker, and Render

Inspired by [render-examples/fastapi](https://github.com/render-examples/fastapi/tree/main)

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
