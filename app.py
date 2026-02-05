from flask import Flask, render_template, request
from utils.pdf_ai import process_pdf, answer_question
from utils.image_ai import extract_text_from_image

app = Flask(__name__)

pdf_text_store = ""

@app.route("/", methods=["GET", "POST"])
def index():
    global pdf_text_store
    summary = ""
    answer = ""
    image_text = ""

    if request.method == "POST":

        # PDF Upload
        if "pdf_file" in request.files:
            pdf = request.files["pdf_file"]
            if pdf.filename != "":
                summary, pdf_text_store = process_pdf(pdf)

        # PDF Question
        question = request.form.get("question")
        if question and pdf_text_store:
            answer = answer_question(question, pdf_text_store)

        # Image Upload
        if "image_file" in request.files:
            image = request.files["image_file"]
            if image.filename != "":
                image_text = extract_text_from_image(image)

    return render_template(
        "index.html",
        summary=summary,
        answer=answer,
        image_text=image_text
    )

if __name__ == "__main__":
    app.run(debug=True)
