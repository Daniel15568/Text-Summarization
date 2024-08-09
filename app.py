from flask import Flask, request, render_template, redirect
import gradio as gr
import fitz
import os
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

#app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("Falconsai/text_summarization")
model = AutoModelForSeq2SeqLM.from_pretrained("Falconsai/text_summarization")
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)


def preprocess_text(text, max_length):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]


def pdf_to_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    subheaders = []
    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        if span["size"] > 12:  # Assuming subheaders have a font size greater than 12
                            subheaders.append(span["text"])
                        text += span["text"] + " "
    return text, subheaders

def summarize(text):
    input_length = len(text.split())
    max_length = max(50, int(input_length / 3))
    summarized_text = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
    return summarized_text[0]['summary_text']


def process_pdf(file):
    text, subheaders = pdf_to_text(file.name)
    parts = preprocess_text(text, 500)
    summaries = [summarize(part) for part in parts]
    full_summary = " ".join(summaries)
    return full_summary, "\n".join(subheaders)

interface = gr.Interface(
    fn=process_pdf,
    inputs=gr.File(label='Upload PDF'),
    outputs=[gr.Textbox(label='Summary'), gr.Textbox(label='Subheaders')],
    title= "PDF Summarizer",
    description="Upload a PDF to get a summarized text")


interface.launch()
# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'file' not in request.files:
#         return redirect(request.url)
#     file = request.files['file']
#     if file.filename == '':
#         return redirect(request.url)
#     if file and file.filename.endswith('.pdf'):
#         upload_folder = './uploads'
#         if not os.path.exists(upload_folder):
#             os.makedirs(upload_folder)
#         file_path = os.path.join(upload_folder, file.filename)
#         file.save(file_path)
#         text = pdf_to_text(file_path)
#         parts = preprocess_text(text, 500)  # Assuming a safe size under model's max length
#         summaries = [summarize(part) for part in parts]
#         full_summary = " ".join(summaries)  # Join all partial summaries
#         return render_template('result.html', summary=full_summary)
#     return redirect(request.url)


# if __name__ == '__main__':
#     app.run(debug=True)

