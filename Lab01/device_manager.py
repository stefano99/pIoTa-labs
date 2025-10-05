import json
import device as device

class DeviceManager:

    def __init__(self):
        self.catalog = json.load(open("Lab01/all.json"))

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
            # print(devices_found)
            return found
        else:
            print("No device found with that name.")

        return found

    def searchByID(self):
        pass

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
            # print(devices_found)
            return found
        else:
            print("No device found with that name.")

    def insertDevice(self):
        user_input_id = input("Enter the new Device ID: ")
        devices_list = self.catalog["devicesList"]
        found = False
        for device in devices_list:
            if device["ID"] == user_input_id:
                found = True

        if found:
            print("Device with this ID already exists.")
        else:
            user_input_name = input("Enter the new Device Name: ")
            user_input_year = input("Enter the new Device Year: ")
            available_services = []
            while True:
                service_to_enter = "Please add the serviceName available. When finish type ok"
                if service_to_enter == "ok":
                    break
                available_services.append(available_services)
        device_dict = {"deviceName":user_input_name,"deviceID":user_input_id,"availableServices":available_services}
        self.catalog["devicesList"].append(device_dict)
        json.dupm(self.catalog,open("all.json","w"))