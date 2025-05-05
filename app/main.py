from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from agent.workflow import run_workflow
import tempfile

app = FastAPI()

@app.post("/generate-pptx")
async def generate_pptx(word_file: UploadFile = File(...), excel_file: UploadFile = File(...)):
    pptx_path = await run_workflow(word_file, excel_file)
    return FileResponse(pptx_path, media_type='application/vnd.openxmlformats-officedocument.presentationml.presentation', filename="output.pptx")