import device_manager as device_manager
import device as device

if __name__ == "__main__":
    welcome_message = "Hello,welcome to the Device Manager"
    list = device_manager.DeviceManager()
    print(welcome_message)
    list.searchByName()