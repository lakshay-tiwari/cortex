import tempfile
from fastapi import APIRouter, UploadFile, File
from app.services.ingestion import ingest_pdf
router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if file.content_type != "application/pdf":
        return {
            "success": False,
            "message": "Only PDF files are supported",
        }

    # Temporarily save uploaded PDF
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        content = await file.read()
        temp_file.write(content)

        file_path = temp_file.name

    # Ingest PDF
    chunks = ingest_pdf(file_path)

    return {
        "success": True,
        "message": "PDF uploaded and indexed successfully",
        "filename": file.filename,
        "chunks": chunks,
    }