import os
import itertools
import re
from parsing.Layout import Layout
from parsing.Output import Output

# function wich parses a layout file into a Layout object
def parse (file):
    file_content = strip_file(file)

    sections = split_to_sections(file_content)

    return convert_sections_to_layout(sections)

# function to split a layout file into the declared sections
def split_to_sections (file_content):
    sections = []

    # split the file content into sections
    for key, group in itertools.groupby(file_content, get_key):
        if key is not False:
            # if the current 'group' is a section declaration, set a new section
            sections += [(key,'')]
        else:
            # if the current 'group' is a series of options bind them to the last section
            # (remove trailing newlines to avoid a empty option caused by a empty line)
            sections[len(sections)-1] = (sections[len(sections)-1][0], ''.join(group).strip('\n'))
    
    return sections

# convert the sections of a layout file into a representation as Layout object
def convert_sections_to_layout (sections):
    layout_name = ''
    layout_settings = {}
    outputs = []

    for section in sections:
        if section[0] == 'Layout':
            # handle the options set in the general Layout section

            # extract the name of the layout
            temp_layout_settings = parse_section_settings(section[1])
            layout_name = temp_layout_settings['name']

            # set all other keys as settings for the layout
            del temp_layout_settings['name']
            layout_settings = temp_layout_settings
        else:
            # parse all other sections as Outputs
            outputs += [Output(section[0], parse_section_settings(section[1]))]

    return Layout(layout_name, layout_settings, outputs)

# function for parsing a section content string with lines of key value pairs into a dictionary
def parse_section_settings(section):
    settings = {}

    # parse every line as setting with a key value pait seperates by a ':'
    for line in section.split(os.linesep):
        setting = line.split('=')

        if len(setting) < 2 :
            # if it is a option without attributes, the attributes string will be set to ''
            settings[setting[0].strip()] = ''
        else:
            settings[setting[0].strip()] = setting[1].strip()

    return settings

# function which extracts the name of the current section from the layout file as key for the groupby function. Returns none if the line
# isn't a section declaration
def get_key (line):
    m = re.match('^\[(\w+)\]$', line)
    
    if m is not None:
        return m.group(1)
    else:
        return False

# function for stripping empty lines and comments out of a file, so it can be parsed easily
# it converts the opened file into an array, so it stays an iterable
def strip_file (file):
    result = []

    for line in file:
        if len(line.strip()) != 0 and not line.strip().startswith('#'):
            result += [line]

    return result
    
