# class which represents a parsed layout file
class Layout:
    def __init__ (self, name, settings, outputs):
        self.name = name
        self.settings = settings
        self.outputs = outputs

    def to_XRandR_String (self):
        result = ""
        
        for key, value in self.settings.items():
            result += "--" + key + " " + value + " "
        for output in self.outputs:
            result += output.toXRandRString()

        return result
