import json
from departments import Department


class RegulationParser:

    def __init__(self):
        self.config_file_path = 'config.json'
        self.departments = {}
        self.config_data = self.load_config()

    def load_config(self):
        with open(self.config_file_path, 'r') as config_file:
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
        return {}

    def get_group(self):
        return {}

    def get_regulation_data(self):
        group = self.get_group()
        paragrapghs = self.get_paragraphs()
        departments = self.get_departments()
        return group, paragrapghs, departments


regulation_parser = RegulationParser()
print(regulation_parser.get_regulation_data())
