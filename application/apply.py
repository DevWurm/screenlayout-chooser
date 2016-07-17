import subprocess

# function for applying a specified layout object to the system settings
def apply (layout):
    # call xrandr with the settings described by the layout object
    subprocess.call(['xrandr'] + layout.to_XRandR_Options())
