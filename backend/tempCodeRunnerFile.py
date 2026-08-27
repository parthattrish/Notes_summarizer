
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

