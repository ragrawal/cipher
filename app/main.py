from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.ciphers import CipherAlgorithm, encrypt_message, decrypt_message, get_cipher_info

app = FastAPI(title="Cipher Web App")

# Mount static files and templates
BASE_DIR = Path(__file__).resolve().parent
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request) -> HTMLResponse:
    """Render the home page with the cipher form."""
    algorithms = [(algo.value, get_cipher_info(algo)) for algo in CipherAlgorithm]
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "algorithms": algorithms,
        },
    )

@app.post("/process", response_class=HTMLResponse)
async def process_message(
    request: Request,
    message: str = Form(...),
    algorithm: CipherAlgorithm = Form(...),
    action: str = Form(...),
) -> HTMLResponse:
    """Process the message using the selected cipher algorithm."""
    algorithms = [(algo.value, get_cipher_info(algo)) for algo in CipherAlgorithm]
    try:
        if action == "encrypt":
            result = encrypt_message(message, algorithm)
        else:
            result = decrypt_message(message, algorithm)
            
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "algorithms": algorithms,
                "result": result,
                "original_message": message,
                "selected_algorithm": algorithm.value,
                "action": action,
                "cipher_info": get_cipher_info(algorithm),
            },
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "algorithms": algorithms,
                "error": str(e),
                "original_message": message,
                "selected_algorithm": algorithm.value,
                "action": action,
            },
        ) 