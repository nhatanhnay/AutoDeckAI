from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_pptx():
    with open("tests/sample.docx", "rb") as wf, open("tests/sample.xlsx", "rb") as xf:
        response = client.post("/generate-pptx", files={"word_file": wf, "excel_file": xf})
        assert response.status_code == 200
        assert response.headers["content-type"] == "application/vnd.openxmlformats-officedocument.presentationml.presentation"