import json
from com.cloudMedia.theKuroBox.sdk.app.module import Module
from com.cloudMedia.theKuroBox.sdk.paramTypes.kbxString import KBXString
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod

class SampleAppModule(Module):
    '''
    Sample Application Module Class.
    '''

    def __init__(self, moduleName, parentPath):
        '''
        Constructor
        Initialize protocol class
        register method which will show in list_api through web server
        '''
        super().__init__(moduleName, parentPath) # This is needed
        self.register_method("get_pyapi", self.get_pyapi)
        self.register_method("printString", self.printString, input=KBXString())
        
    
    def get_pyapi(self, request):
        pyapi = SharedMethod.get_pyapi()
        returnData = {}
        returnData["pyapi"] = pyapi
        self.send_response(returnData, request.requestId)
        
    
    def printString(self, request):
        # Get value pass in for this parameter
        input = request.get_arg("input")
        
        print("func printString: ", input)
        
        # Response to requester
        self.send_response({"success":True}, request.requestId)
        
        
    def on_system_connected(self):
        '''
        Implement body when the application is connected to the system
        Developer should put their code for dealing with system here, such as:
        - Register Event
        - Register Event Listener
        - Register Shared Method

        For System Connected timing in Module, please refer to Module.on_system_connected
        '''
        pass

    def post_system_connected(self):
        '''
        Implement body when the on_system_connected timing is finished
        This timing is located after on_system_connected timing in application and all modules
        '''
        pass