from fastapi import FastAPI
from llama_cpp import Llama
import os
import uvicorn

app = FastAPI()

model_path = os.getenv("MODEL_PATH", "model/DeepSeek-R1-Distill-Qwen-1.5B-Q4_1.gguf")

llm = Llama(
    model_path=model_path,
    n_ctx=4096,
    n_threads=4
)

@app.post("/infer")
async def infer(payload: dict):
    prompt = payload.get("prompt", "")
    output = llm(
        prompt,
        max_tokens=512,
        temperature=0.7
    )
    return {"response": output["choices"][0]["text"]}

if __name__ == "__main__":
    # Listen on all interfaces so SAP AI Core can reach it
    uvicorn.run(app, host="0.0.0.0", port=8000)
