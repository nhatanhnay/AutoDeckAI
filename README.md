# AutoDeckAI

Tự động tạo slide PowerPoint từ file Word và Excel bằng AI (Gemini).

## Tính năng
- Trích xuất nội dung từ Word
- Phân tích số liệu từ Excel
- Sinh biểu đồ trực quan
- Tạo slide trình bày đẹp mắt

## Chạy thử
```bash
uvicorn app.main:app --reload
```

## Sử dụng Docker
```bash
docker build -t autodeckai .
docker run -p 8000:8000 autodeckai
```

## Gọi API
`POST /generate-pptx`

Form-data:
- `word_file`: file .docx
- `excel_file`: file .xlsx

Kết quả trả về là file `.pptx`
