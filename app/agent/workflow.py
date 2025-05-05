import tempfile
from .word_parser import extract_text_from_word
from .excel_analyzer import analyze_excel_data
from .ppt_generator import generate_ppt

async def run_workflow(word_file, excel_file):
    word_bytes = await word_file.read()
    excel_bytes = await excel_file.read()

    word_text = extract_text_from_word(word_bytes)
    analysis_result, plot_path = analyze_excel_data(excel_bytes)

    pptx_path = generate_ppt(word_text, analysis_result, plot_path)
    return pptx_path