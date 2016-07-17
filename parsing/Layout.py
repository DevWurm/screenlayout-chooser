# class which represents a parsed layout file
class Layout:
    def __init__ (self, name, settings, outputs):
        self.name = name
        self.settings = settings
        self.outputs = outputs

    # convert all settings into an options array which can be passed to xrandr
    def to_XRandR_Options (self):
        result = [] 
        
        # set every option as key value pair
        for key, value in self.settings.items():
            result += ["--" + key, value]
        # append the options for every output
        for output in self.outputs:
            result += output.to_XRandR_Options()

        # remove all empty entries in the array (every option without arguments [like --primary] is followed by an empty string
        # what causes xrandr to throw an error)
        return list(filter(bool, result))
