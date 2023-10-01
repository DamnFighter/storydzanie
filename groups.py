import PyPDF2
import re


class Groups:
    def __init__(self, file_path, start_string, end_string):
        self.pdf_file_path = file_path
        self.start_string = start_string
        self.end_string = end_string
        self.text = ""

    def get_text_for_group(self):
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

    def get_groups_list(self):
        self.get_text_for_group()
        pattern = r'(\d+(?:, \d+)*)'
        matches = re.findall(pattern, self.text, re.MULTILINE)
        result_list = matches[0].split(", ")
        return result_list
