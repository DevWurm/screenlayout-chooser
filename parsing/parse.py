import itertools
import re
from Layout import Layout
from Output import Output
import string

# function wich parses a layout file into a Layout object
def parse (file):
    sections = split_to_sections(file)

    return convert_sections_to_layout(sections)

# function to split a layout file into the declared sections
def split_to_sections (file):
    sections = []

    with open(file) as f:
        for key, group in itertools.groupby(f, get_key):
            if key is not False:
                sections += [(key,'')]
            else:
                sections[:1][0][1] = ''.join(group)
    
    return sections

# convert the sections of a layout file into a representation as Layout object
def convert_sections_to_layout (sections):
    layout_name = ''
    layout_settings = {}
    outputs = []

    for section in sections:
        if section[0] is 'Layout':
            temp_layout_settings = parse_section_settings(section[1])
            layout_name = temp_layout_settings['name']

            del temp_layout_settings['name']
            layout_settings = temp_layout_settings
        else:
            outputs += [Output(section[0], parse_section_settings(section[1]))]

    return Layout(layout_name, layout_settings, outputs)

# function for parsing a section content string with lines of key value pairs into a dictionary
def parse_section_settings(section):
    settings = {}

    for line in string.split(section, '\n'):
        setting = string.split(line, ':')

        if len(setting) < 2 :
            # if it is a option without attributes, the attributes string will be set to ''
            settings[setting[0].strip()] = ''
        else:
            settings[setting[0].strip()] = setting[1].strip()

    return settings

# function which extracts the name of the current section from the layout file as key for the groupby function. Returns none if the line
# isn't a section declaration
def get_key (line):
    m = re.match('^\[(\w+\]$', line)
    
    if m is not None:
        return m.group(1)
    else:
        return False
