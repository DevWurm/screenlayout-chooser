# class which describes a XRandR output
class Output:
    def __init__ (self, name, settings):
        self.name = name
        self.settings = settings

    # convert all settings into an options array which can be passed to xrandr
    def to_XRandR_Options (self):
        # set the output
        result = ["--output", self.name]

        # set every option as key value pair
        for key, value in self.settings.items():
            result += ["--" + key, value]

        # remove all empty entries in the array (every option without arguments [like --primary] is followed by an empty string
        # what causes xrandr to throw an error)
        return list(filter(bool, result))
