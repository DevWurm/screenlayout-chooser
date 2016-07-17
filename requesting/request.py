import subprocess
import re
from functools import reduce

def request(request_layouts, request_options):
    rofi_input_string = reduce(lambda res, nxt: res + '\n' + nxt, map(lambda lay: lay.name, request_layouts))

    rofi = subprocess.Popen(['rofi', '-dmenu'] + request_options, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)

    chosen_layout_string = (rofi.communicate(input=rofi_input_string.encode('UTF-8'))[0]).decode('UTF-8').strip('\n')

    return chosen_layout_string

def get_request_options(bg_color, text_color, inactive_bg_color, inactive_text_color, font):
    padding = str(get_screen_height() / 3)

    request_options= ['-lines', '3',\
                    '-eh', '2',\
                    '-width', '100',\
                    '-padding', padding,\
                    '-opacity', '90',\
                    '-bw', '0',\
                    '-color-enabled',\
                    '-color-window', inactive_bg_color + ', ' + inactive_bg_color,\
                    '-color-normal', inactive_bg_color + ', ' + inactive_text_color + ', ' + inactive_bg_color + ', ' + bg_color + ', ' + text_color,\
                    '-color-urgent', inactive_bg_color + ', ' + inactive_text_color + ', ' + inactive_bg_color + ', ' + bg_color + ', ' + text_color,\
                    '-color-active', inactive_bg_color + ', ' + inactive_text_color + ', ' + inactive_bg_color + ', ' + bg_color + ', ' + text_color,\
                    '-font', font]

    return request_options

def get_screen_height ():
    xwininfo_output = subprocess.check_output(['xwininfo', '-root']).decode('UTF-8')
    for line in xwininfo_output.split('\n'):
        if re.search('Height:', line):
            return int(line.split(':')[1].strip())
