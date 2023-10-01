import json
from departments import Department
from paragraphs import Paragraphs
from groups import Groups

class RegulationParser:

    def __init__(self):
        self.config_file_path = 'config.json'
        self.departments = {}
        self.paragraphs = {}
        self.config_data = self.load_config()

    def load_config(self):
        with open(self.config_file_path, 'r', encoding="UTF-8") as config_file:
            return json.load(config_file)

    def get_departments(self):
        for department_config in self.config_data['departments']:
            key = department_config['key']
            department_name = department_config['department_name']
            next_department_name = department_config['next_department_name']
            file_path = department_config['file_path']

            department_instance = Department(file_path, department_name, next_department_name)
            self.departments[key] = department_instance.get_chapters_list()
            return self.departments

    def get_paragraphs(self):
        for paragraphs_config in self.config_data['paragraphs']:
            key = paragraphs_config['key']
            start_string = paragraphs_config['start_string']
            end_string = paragraphs_config['end_string']
            file_path = paragraphs_config['file_path']

            paragraphs_instance = Paragraphs(file_path, start_string, end_string)
            self.paragraphs[key] = paragraphs_instance.get_paragraphs_list()
        return self.paragraphs

    def get_groups(self):
        for groups_config in self.config_data['groups']:
            key = groups_config['key']
            start_string = groups_config['start_string']
            end_string = groups_config['end_string']
            file_path = groups_config['file_path']

            groups_instance = Groups(file_path, start_string, end_string)
            self.groups = groups_instance.get_groups_list()
        return self.groups

    def get_regulation_data(self):
        groups = self.get_groups()
        paragraphs = self.get_paragraphs()
        departments = self.get_departments()
        return groups, paragraphs, departments

if __name__ == "__main__":
    regulation_parser = RegulationParser()
    print(regulation_parser.get_regulation_data())
