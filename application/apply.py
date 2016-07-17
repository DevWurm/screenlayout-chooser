import subprocess

def apply (layout):
    subprocess.call(['xrandr'] + layout.to_XRandR_Options())
