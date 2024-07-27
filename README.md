# PDF Text Summarization

PDF Text Summarization is a web application that allows users to upload PDF files and get summarized text using a pre-trained NLP model. The application uses the Hugging Face Transformers library and Flask for the backend server.

## Features

- Upload a PDF file and receive a summarized version of its text content.
- Uses a pre-trained summarization model from Hugging Face.
- Simple and intuitive web interface.

## Installation

#### Set Up the Virtual Environment

Using Anaconda:
    `conda create --name myenv python=3.10
    conda activate myenv`

#### Install Dependencies
    pip install -r requirements.txt
#### Run the Application
    flask run
Open your browser and navigate to http://127.0.0.1:5000.

### Prerequisites

- Python 3.7 or higher
- Anaconda or virtualenv for managing dependencies

### Clone the Repository
`git clone https://github.com/Daniel15568/Text-Summarization.git`

## Usage
- Open the web application in your browser.
- Upload a PDF file by clicking the "Choose File" button and selecting your PDF.
- Click the "Upload" button to submit the file.
- The application will process the file and display a summarized version of the text.

## Dependencies
Flask: A micro web framework for Python.
PyMuPDF (fitz): A library to read, manipulate, and convert PDF files.
Transformers: Hugging Face library for state-of-the-art NLP models.
Torch: A deep learning framework for NLP models.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

### Possible additions
- Include word files
- Add pssible subtopics
- Restructure html file with css (web-dev)

## License
This project is licensed under the GNU License. See the LICENSE file for details.


*This project was created as part of a learning exercise in hugging face transformers and flask framework.*
