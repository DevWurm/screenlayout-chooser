# class which describes a XRandR output
class Output:
    def __init__ (self, name, settings):
        self.name = name
        self.settings = settings

    def to_XRandR_String (self):
        result = "--output " + self.name + " "

        for key, value in self.settings.items():
            result += "--" + key + " " + value + " "

        return result
