import fitz
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

def extract_text_from_pdf_pymupdf(pdf_path):
    try:
        text = ""
        with fitz.open(pdf_path) as doc:
            for page_num in range(doc.page_count):
                text += doc.load_page(page_num).get_text()
        return text
    except Exception as e:
        print(f"An error occurred while extracting text from the PDF: {e}")
        return ""

def ai_recruiter_agent(extracted_text):
    gemini_client = genai.Client(api_key=gemini_api_key)
    
    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            {
                "role": "user",
                "parts": [
                    {
                        "text": (
                            "You are an expert AI recruiter. Carefully analyze the provided resume text, "
                            "then rewrite and improve the entire resume to maximize its impact for AI and technology recruiter positions. "
                            "Format the improved resume using LaTeX, ensuring that it is clean, professional, and well-structured. "
                            "Only output the complete LaTeX code for the improved resume.\n\n"
                            f"Resume text to analyze and improve:\n{extracted_text}"
                        )
                    }
                ]
            }
        ]
    )
    return response.text

def save_latex_to_file(latex_code, filename):
    with open(filename, "w") as file:
        file.write(latex_code)

if __name__ == "__main__":
    pdf_file = "./resume.pdf"
    extracted_text = extract_text_from_pdf_pymupdf(pdf_file)
    latex_code = ai_recruiter_agent(extracted_text)
    print(latex_code)
    save_latex_to_file(latex_code, "improved_resume.tex")