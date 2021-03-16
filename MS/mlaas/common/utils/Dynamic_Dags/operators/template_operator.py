from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults
import re
import requests
import json
import uuid

class TemplateOperator(BaseOperator):

    @apply_defaults
    def __init__(
        self,
        template_file_path=None,
        destination_file_path=None,
        search_and_replace=None,
        *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.template_file_path = template_file_path
        self.destination_file_path = destination_file_path
        self.search_and_replace = search_and_replace

    def execute(self,context=None):
        content = None
        
        print("Creating template")
        
        with open(self.template_file_path, 'r', encoding = 'utf-8') as template:
            content = template.read()

        for key, value in self.search_and_replace.items():
            content = re.sub(key, value, content)

        with open(self.destination_file_path, 'w', encoding = 'utf-8') as destination:
            destination.write(content)
        
        # print(f"Template Creation Complete. Created a dag with name {self.search_and_replace['#DAG_ID']} .")
        print("Process Complete.")
        return