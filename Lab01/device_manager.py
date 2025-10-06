import json
from datetime import datetime
# import device as device

class DeviceManager:

    def __init__(self):
        self.catalog = json.load(open("Lab01/catalog.json"))

    def searchByName(self):
        user_input = input("Enter the device name to search: ")
        devices_list = self.catalog["devicesList"]
        devices_found = []
        found = False

        for device in devices_list:
            if device["deviceName"] == user_input:
                print(f"Device found: Name: {device['deviceName']}, ID: {device['deviceID']}")
                devices_found.append(device)
                found = True
        
        if found:
            print(devices_found)
        else:
            print("No device found with that name.")
        return found

    def searchByID(self):
        user_input = input("Enter the device ID to search: ")
        devices_list = self.catalog["devicesList"]
        devices_found = []
        found = False

        for device in devices_list:
            if device["deviceID"] == user_input:
                print(f"Device found: Name: {device['deviceName']}, ID: {device['deviceID']}")
                devices_found.append(device)
                found = True
        
        if found:
            print(devices_found)
        else:
            print("No device found with that ID.")
        return found

    def searchByService(self):
        user_input = input("Enter the device service type to search: ")
        devices_list = self.catalog["devicesList"]
        devices_found = []
        found = False

        for device in devices_list:
            if device["serviceType"] == user_input:
                print(f"Device found: Name: {device['deviceName']}, ID: {device['deviceID']}")
                devices_found.append(device)
                found = True
        
        if found:
            print(devices_found)
        else:
            print("No device found with that service type.")
        return found
    
    def searchByMeasureType(self):
        user_input = input("Enter the device measure type to search: ")
        devices_list = self.catalog["devicesList"]
        devices_found = []
        found = False

        for device in devices_list:
            if device["measureType"] == user_input:
                print(f"Device found: Name: {device['deviceName']}, ID: {device['deviceID']}")
                devices_found.append(device)
                found = True
        
        if found:
            print(devices_found)
        else:
            print("No device found with that measure type.")
        return found

# INCOMPLETE
    def insertDevice(self):
        user_input_id = input("Enter the new Device ID: ")
        devices_list = self.catalog["devicesList"]
        found = False

        # check if device with same ID already exists
        for device in devices_list:
            if device["deviceID"] == user_input_id:
                found = True

        # if the device ID already exists, ask user for update
        if found:
            print("Device with this ID already exists.")

        # if the device ID does not exist, ask user for device details
        else:
            user_input_name = input("Enter the new Device Name: ")

            measure_types = []
            available_services = []
            service_details = []


            # ask user for available measureTypes until they type 'ok'
            while True:
                measure_type_to_enter = input("Please add the measureType available. When finish type ok: ")
                if measure_type_to_enter == "ok":
                    break
                measure_types.append(measure_type_to_enter)

            # ask user for available services until they type 'ok'
            while True:
                service_to_enter = input("Please add the serviceType available. When finish type ok: ")
                if service_to_enter == "ok":
                    break
                single_detail_to_enter = []
                # for each service, ask user for serviceDetails until they type 'ok'
                while True:
                    detail_to_enter = input("Please add the serviceDetails available for the Service you just added. When finish type ok: ")
                    if detail_to_enter == "ok":
                        break
                    single_detail_to_enter.append(detail_to_enter)
                if service_to_enter == "MQTT":
                    single_service_details_to_enter = {"serviceType":service_to_enter,"topic":single_detail_to_enter}
                elif service_to_enter == "REST":
                    single_service_details_to_enter = {"serviceType":service_to_enter,"serviceIP":single_detail_to_enter}  

                # update serviceDetails list
                service_details.append(single_service_details_to_enter)
                # update availableServices list
                available_services.append(service_to_enter)
                
            # update lastUpdate field of the newly added device to current date and time
            last_update = datetime.now().strftime("%Y-%m-%d %H:%M")


        device_dict = {"deviceID":user_input_id,"deviceName":user_input_name,"measureType":measure_types,"availableServices":available_services,"lastUpdate":last_update}
        self.catalog["devicesList"].append(device_dict)

        # update lastUpdate field of the whole documentto current date and time
        self.catalog["lastUpdate"] = datetime.now().strftime("%Y-%m-%d %H:%M")

    def printAll(self):
        print(self.catalog)
        
    def exit(self):
        print("Exiting the Device Manager.\nSaving catalog to catalog.json")
        json.dump(self.catalog,open("catalog_updated.json","w"))
        exit(0)