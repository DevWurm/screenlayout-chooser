# screenlayout-chooser
Conveniently define, choose and apply screenlayouts.

In power user linux distros like Arch Linux there is no default for configuring and applying screenlayouts easily. XRandR is a 
cli tool for achieving this but it requires a lot of keypresses to initiate the layout change and XRandR shell scripts are not very nicely
configurable, due to the length of the calls and the thereby resulting amount of scrolling through the command. There are also graphical
tools like ARandR, which make switching layouts easier, but still require a lot of interactions.

screenlayout-chooser is a Python3 script which accepts a folder, which contains layout definitions in the easy to write and understandable
[INI file format](https://en.wikipedia.org/wiki/INI_file). It then shows a small graphical interface via rofi, which lets you choose your
layout with only a few keypresses. It then applies the chosen layout via XRandR.

## Installation
Install the [dependencies](#dependencies). You can copy the needed files and directories (`layout-chooser`, `layout-applier`, `application`, `parsing` and `requesting`) into an appropriate location.\
You can also install it automatically using `make`.\
To install it into your user scope (to `~/.scripts/screenlayout-chooser`) call
```
make install
```
in the project directory.\
To install it in the global scope (to `/opt/scripts/screenlayout-chooser`) call
```
make installGlobal
```
in the project directory with write permissions to this directory.

### Dependencies
To use screenlayout-chooser, you need the executables of the following tools in your PATH:
* [rofi](https://davedavenport.github.io/rofi/)
* [xorg-xrandr](https://www.x.org/wiki/Projects/XRandR/) (probably allready installed)
* [xorg-xwininfo](http://linux.die.net/man/1/xwininfo) (also probably installed)

## Usage
To use the layout chooser call:
```
layout-chooser [dir] [active-background-color] [active-text-color] [inactive-background-color] [inactive-text-color] "[font] [font-size]"
```
with python 3 as `python` in your path.\
`dir` references the directory, where your layout files rest.\
A pretty nice configuration is:
```
layout-chooser [dir] #2F343F #9575cd #2F343F #F3F4F5 "[font] 30"
```
It's also possible to apply a specific layout file by calling:
```
layout-applier [path-to-layout-file]
```

### Layout files
Layout files are built by sections (identifiers between `[]` brackets, followed by `key=value` pairs). Each section will be understood as
an XRandR ouput and the following options as XRandR options and their values for this output. Options without arguments (i.e. `primary`)
are only defined as `key`. There is one section which is handles a bit differently. The `Layout` section is not converted to an output.
It's `name` option is used as display name for the chooser and all other options are inserted one time into the call (i.e. the 
`noprimary` option).\
So the file:
```
[Layout]
name=TestLayout

[eDP1]
primary
mode= 2560x1440
pos= 2048x180
rotate= normal

[HDMI1]
mode= 1920x1080
pos= 4608x0
rotate=normal
scale= 1.5x1.5

[DP2]
mode= 1024x768
pos= 0x84
rotate= normal
scale= 2x2
```
will result in this XRandR call:
```
xrandr --output eDP1 --primary --mode 2560x1440 --pos 2048x180 --rotate normal --output HDMI1 --mode 1920x1080 --pos 4608x0 --rotate normal --scale 1.5x1.5 --output DP2 --mode 1024x768 --pos 0x84 --rotate normal --scale 2x2
```
and is displayed as `TestLayout` in the chooser.

##License
'screenlayout-chooser' is offered under MIT License (Read LICENSE). USe it! :)<br>
Copyright 2016 DevWurm

##Collaborating
I really appreciate any kind of collaboration!<br>
You can use the [GitHub issue tracker](https://github.com/DevWurm/screenlayout-chooser/issues) for bugs and feature requests or [create a pull request](https://github.com/DevWurm/screenlayout-chooser/pulls) to submit
changes. Forks are welcome, too!
If you don't want to use these possibilities, you can also write me an email to
<a href='mailto:devwurm@devwurm.net'>devwurm@devwurm.net</a>.

## Contact
If you have any questions, ideas, etc. feel free to contact me:<br>
DevWurm<br>
Email: <a href='mailto:devwurm@devwurm.net'>devwurm@devwurm.net</a><br>
Jabber: devwurm@jabber.ccc.de<br>
Twitter: @DevWurm<br>
