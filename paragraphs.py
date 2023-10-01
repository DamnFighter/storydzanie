import PyPDF2
import re


class Paragraphs:
    def __init__(self, file_path, start_string, end_string):
        self.pdf_file_path = file_path
        self.start_string = start_string
        self.end_string = end_string
        self.text = ""

    def get_text_for_paragraph(self):
        with open(self.pdf_file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            found_start = False
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                if self.start_string in page_text:
                    found_start = True
                    page_text = page_text.split(self.start_string)[1]
                    text += self.start_string
                if found_start:
                    if self.end_string in page_text:
                        page_text = page_text.split(self.end_string)[0]
                        found_start = False
                    text += page_text
        self.text = text.strip()

    def get_paragraphs_list(self):
        self.get_text_for_paragraph()
        pattern = r'(\d{3})\s([A-ZŁŚŻ][a-ząćęłńóśżź]+)\s(.*?)$'
        matches = re.findall(pattern, self.text, re.MULTILINE)
        result_list = [{'paragraf': match[0], 'tytul': " ".join(match[1:])} for match in matches]
        return result_list
