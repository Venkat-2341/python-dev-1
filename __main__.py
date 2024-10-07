from orderProcessing import GlobalConstants, GlobalConfiguration

if __name__ == "__main__":
    try:
        GlobalConfiguration.get_configuration()
        ordersDataFolder = GlobalConfiguration.configuration[GlobalConstants.ORDERS_DATA_FOLDER]
        customersDataFolder = GlobalConfiguration.configuration[GlobalConstants.CUSTOMERS_SERVICE_URL]
        productsDataFile = GlobalConfiguration.configuration[GlobalConstants.PRODUCTS_DATA_FILE] 
 
        print(f'Orders Data Folder : ${ordersDataFolder}')
        print(f'Customers Service URL : ${customersDataFolder}')
        print(f'Products Data File : ${productsDataFile}')
        
    except Exception as Error:
        print('Error occured, Details : {}'.format(str(Error)))
        