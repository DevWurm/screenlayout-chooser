# class which represents a parsed layout file
class Layout:
    def __init__ (self, name, settings, outputs):
        self.name = name
        self.settings = settings
        self.outputs = outputs

    def to_XRandR_Options (self):
        result = [] 
        
        for key, value in self.settings.items():
            result += ["--" + key, value]
        for output in self.outputs:
            result += output.to_XRandR_Options()

        return list(filter(bool, result))
