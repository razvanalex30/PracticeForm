from robot.libraries.BuiltIn import BuiltIn

class SeleniumLibraryExt:
    

    def driver1(self):
        return BuiltIn().get_library_instance('SeleniumLibrary').driver
        
    # @classmethod
    # def create_driver(cls):
        # return BuiltIn().get_library_instance('SeleniumLibrary').driver