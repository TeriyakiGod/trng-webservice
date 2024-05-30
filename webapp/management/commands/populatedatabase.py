import os
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from matplotlib import category
from ...models import RandTool

class Command(BaseCommand):
    help = 'Loads rand tools from XML file into the database'

    def handle(self, *args, **options):
        # Path to the XML file in the static folder
        xml_file_path = os.path.join('static', 'rand_tools.xml')

        # Check if the XML file exists
        if not os.path.exists(xml_file_path):
            self.stdout.write(self.style.ERROR('XML file does not exist'))
            return

        # Parse the XML file
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # Iterate through XML elements and create or update RandTool objects
        for tool_elem in root.findall('rand_tool'):
            name = tool_elem.find('name').text
            path = tool_elem.find('path').text
            short_description = tool_elem.find('short_description').text
            description = tool_elem.find('description').text
            category = tool_elem.find('category').text

            # Check if the tool already exists in the database
            existing_tool = RandTool.objects.filter(name=name).first()
            if existing_tool:
                # Update the existing tool
                existing_tool.path = path
                existing_tool.short_description = short_description
                existing_tool.description = description
                existing_tool.category = category
                existing_tool.save()
            else:
                # Create a new tool
                RandTool.objects.create(name=name, path=path, short_description=short_description, description=description)

        self.stdout.write(self.style.SUCCESS('Rand tools loaded successfully'))
