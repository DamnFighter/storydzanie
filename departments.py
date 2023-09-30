import PyPDF2
import re

class Department:
    def __init__(self, file_path, department_name, next_department_name):
        self.pdf_file_path = file_path
        self.department_name = department_name
        self.next_department_name = next_department_name
        self.text = ""


    def get_text_for_department(self):
        with open(self.pdf_file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            found_start = False
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                if self.department_name in page_text:
                    found_start = True
                    page_text = page_text.split(self.department_name)[1]
                    text += self.department_name
                if found_start:
                    if self.next_department_name in page_text:
                        page_text = page_text.split(self.next_department_name)[0]
                        found_start = False
                    text += page_text
        self.text = text.strip()


    def get_chapters_list(self):
        self.get_text_for_department()
        pattern = r'(\d{5})\s(.*?)(?=\s\d{5}\s|$|(?=\d{5}\s))'
        matches = re.findall(pattern, self.text, re.DOTALL)
        result_list = [{'rozdzial': match[0], 'tytul': match[1].strip()} for match in matches]
        return result_list
