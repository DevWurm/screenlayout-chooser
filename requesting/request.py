import subprocess
import re
from functools import reduce

# perform a visual request to the user via rofi, with the content provided via request_layouts
def request(request_layouts, request_options):
    # extract the layout names from the layout objects and concatenate them seperated by '\n'
    rofi_input_string = reduce(lambda res, nxt: res + '\n' + nxt, map(lambda lay: lay.name, request_layouts))

    # start the rofi process with the according options
    rofi = subprocess.Popen(['rofi', '-dmenu'] + request_options, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)

    # pipe the layout names into rofis stdin and recieve the ouput from its stdout (remove the trailing newline, because it doesn't
    # belong to the layout name itself)
    chosen_layout_string = (rofi.communicate(input=rofi_input_string.encode('UTF-8'))[0]).decode('UTF-8').strip('\n')

    return chosen_layout_string

# generate an array of options which can be passed to rofi
def get_request_options(bg_color, text_color, inactive_bg_color, inactive_text_color, font):
    # calculate the padding of the rofi menu by the current screen height and an arbitrary factor
    padding = str(get_screen_height() / 3)

    request_options= ['-p', 'layout',\
                    '-lines', '3',\
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

# get the current screen height by the xwininfo command
def get_screen_height ():
    xwininfo_output = subprocess.check_output(['xwininfo', '-root']).decode('UTF-8')
    for line in xwininfo_output.split('\n'):
        if re.search('Height:', line):
            return int(line.split(':')[1].strip())
