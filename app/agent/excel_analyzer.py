import pandas as pd
import matplotlib.pyplot as plt
import tempfile
import io
import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def analyze_excel_data(excel_bytes):
    df = pd.read_excel(io.BytesIO(excel_bytes))
    stats = df.describe().to_string()

    prompt = f"Phân tích các điểm nổi bật trong dữ liệu sau:\n{stats}"
    response = model.generate_content(prompt)

    plot_path = tempfile.mktemp(suffix=".png")
    df.hist(figsize=(10, 6))
    plt.tight_layout()
    plt.savefig(plot_path)

    return response.text, plot_path