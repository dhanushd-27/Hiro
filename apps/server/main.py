import fitz
from dotenv import load_dotenv
from google import genai
import os
import sys

def load_api_key():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY not found in environment variables.")
    return api_key

def extract_text_from_pdf_pymupdf(pdf_path):
    text = []
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text.append(page.get_text())
        return "\n".join(text)
    except Exception as e:
        print(f"An error occurred while extracting text from the PDF: {e}", file=sys.stderr)
        return ""

def ai_recruiter_agent(extracted_text, gemini_api_key):
    if not extracted_text.strip():
        raise ValueError("No text extracted from PDF. Cannot proceed with AI recruiter agent.")

    gemini_client = genai.Client(api_key=gemini_api_key)

    prompt = (
        "You are an expert AI recruiter. Carefully analyze the provided resume text, "
        "then rewrite and improve the entire resume to maximize its impact for AI and technology recruiter positions. "
        "Format the improved resume using LaTeX, ensuring that it is clean, professional, and well-structured. "
        "Only output the complete LaTeX code for the improved resume.\n\n"
        f"Resume text to analyze and improve:\n{extracted_text}"
    )

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            {
                "role": "user",
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    )
    return getattr(response, "text", "")

def save_latex_to_file(latex_code, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(latex_code)
    except Exception as e:
        print(f"Error saving LaTeX to file {filename}: {e}", file=sys.stderr)

def main(pdf_file, output_file="improved_resume.tex"):
    gemini_api_key = load_api_key()
    extracted_text = extract_text_from_pdf_pymupdf(pdf_file)

    if not extracted_text:
        print("Failed to extract any text from the provided PDF. Exiting.", file=sys.stderr)
        sys.exit(1)

    latex_code = ai_recruiter_agent(extracted_text, gemini_api_key)

    if not latex_code.strip():
        print("Failed to generate improved LaTeX resume. Exiting.", file=sys.stderr)
        sys.exit(1)

    print("Generated LaTeX Resume:\n")
    print(latex_code)
    save_latex_to_file(latex_code, output_file)
    print(f"\nLaTeX resume saved to {output_file}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Rewrite and improve a resume PDF using Gemini AI, outputting a LaTeX version.")
    parser.add_argument("pdf_file", help="Path to the input resume PDF file.")
    parser.add_argument("--output", "-o", default="improved_resume.tex", help="Output .tex filename (default: improved_resume.tex)")

    args = parser.parse_args()
    main(args.pdf_file, args.output)