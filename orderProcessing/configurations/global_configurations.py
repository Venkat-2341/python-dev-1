import os
from ..constants import GlobalConstants 

INVALID_ORDERS_DATA_FOLDER = 'INVALID ORDERS DATA FOLDER SPECIFIED!'
INVALID_CUSTOMER_SERVICE_URL = 'INVALID CUSTOMER SERVICE URL SPECIFIED!'
INVALID_PRODUCTS_DATA_FILE = 'INVALID PRODUCTS DATA FILE SPECIFIED!'

# os.environ.get --> It is a dictionary in Python that contains the system’s environment variables.

class GlobalConfiguration:
    configuration = {}
    
    # you don't need an object to access this function
    # we can just do GlobalConfiguration.get_configuration()
    @staticmethod
    def get_configuration():
        isConfigurationNull = GlobalConfiguration.configuration is not None
        configurationLength = GlobalConfiguration.configuration.__len__()
        
        validation = isConfigurationNull and (configurationLength<=0)   
        
        # check if the configuration is already there
        if not validation:
            return GlobalConfiguration.configuration
        
        ordersDataFolder = os.environ.get(GlobalConstants.ORDERS_DATA_FOLDER, None)  
        if ordersDataFolder is None:
            raise Exception(INVALID_ORDERS_DATA_FOLDER)
        
        customersDataFolder = os.environ.get(GlobalConstants.CUSTOMERS_SERVICE_URL, None)
        if customersDataFolder is None:
            raise Exception(INVALID_CUSTOMER_SERVICE_URL)
         
        productsDataFile = os.environ.get(GlobalConstants.PRODUCTS_DATA_FILE, None)
        if productsDataFile is None:
            raise Exception(INVALID_PRODUCTS_DATA_FILE)
        
        GlobalConfiguration.configuration[GlobalConstants.ORDERS_DATA_FOLDER] = ordersDataFolder
        GlobalConfiguration.configuration[GlobalConstants.CUSTOMERS_SERVICE_URL] = customersDataFolder
        GlobalConfiguration.configuration[GlobalConstants.PRODUCTS_DATA_FILE] = productsDataFile
        
        return GlobalConfiguration.configuration
