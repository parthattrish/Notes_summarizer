from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

import os
import shutil

from backend.pdf_reader import extract_text_from_pdf
from backend.summarizer import summarize_text
from backend.pdf_generator import generate_pdf

app = FastAPI(
    title="AI Notes Summarizer",
    version="1.0"
)

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "backend/uploads"
OUTPUT_FOLDER = "backend/generated"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "AI Notes Summarizer Backend Running!"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Please upload a PDF file."}

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    extracted_text = extract_text_from_pdf(file_path)

    # AI Summary
    summary = summarize_text(extracted_text)

    # Output PDF
    output_pdf = os.path.join(
        OUTPUT_FOLDER,
        f"summary_{file.filename}"
    )

    generate_pdf(summary, output_pdf)

    return {
        "filename": file.filename,
        "summary": summary,
        "pdf_path": f"/download/{os.path.basename(output_pdf)}"
    }


@app.get("/download/{filename}")
def download(filename: str):

    path = os.path.join(OUTPUT_FOLDER, filename)

    return FileResponse(
        path,
        media_type="application/pdf",
        filename=filename
    )
