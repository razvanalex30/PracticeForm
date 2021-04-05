from robot.libraries.BuiltIn import BuiltIn

class SeleniumLibraryExt:
    
    @classmethod
    def create_driver(cls):
        return BuiltIn().get_library_instance('SeleniumLibrary').driver