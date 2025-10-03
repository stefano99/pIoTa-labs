from datetime import datetime

class temperatureSensor:
    def __init__(self, name, sensorID, fabricationYear, calibstatus=False, measurements=None):
        self.name = name
        self.sID = sensorID
        self.fabYear = fabricationYear
        self.calibrated = calibstatus
        self.measurements = measurements # List to store measurements
    
    def printInfo(self):
        print(f"Sensor Name: {self.name}, Sensor ID: {self.sID}, Fabrication Year: {self.fabYear}")

    def getAge(self):
        # Simulate reading a value from the sensor
        currentYear = datetime.now().year
        age = currentYear - self.fabYear
        return age # Return the age of the sensor
    
    def isCalibrated(self):
        return self.calibrated # Return calibration status
    
    # OVERWRITES FILE CONTENTS (if no file, it creates one)
    def writeToFile(self, filename="sensors.txt"): # default filename is sensors.txt
        f = open(filename, "w") # Open the file in write mode
        f.write(f"{self.name},{self.sID},{self.fabYear}\n")
        f.close()

    # APPENDS at the bottom of the file (if no file, it creates one)
    def appendToFile(self, filename="sensors.txt"): # default filename is sensors.txt
        f = open(filename, "a") # Open the file in append mode
        f.write(f"{self.name},{self.sID},{self.fabYear}\n")
        f.close()
    
    def readFromFile(self, filename):
        f = open(filename, "r") # Open the file in read mode
        content = f.read() # Read the first line
        f.close()
        
        attributes = content.split(',')
        self.name = attributes[0]
        self.sID = attributes[1]
        self.fabYear = int(attributes[2])
        if len(attributes) > 3:
            self.calibrated = attributes[3].strip().lower() == 'true'
        else:
            self.calibrated = False

    def readMeasurementsFromFile(self, filename):
        self.measurements = []
        f = open(filename, "r") # Open the file in read mode
        content = float(f.read().split(',')) # Read all lines, but should be a single line
        f.close()
        self.measurements.append(content)

    def getMeanMeasurement(self):
        if self.measurements is None or len(self.measurements) == 0:
            return None
        return sum(self.measurements) / len(self.measurements)
    
    def getMinMeasurement(self):
        if self.measurements is None or len(self.measurements) == 0:
            return None
        return min(self.measurements)   
    
    def getMaxMeasurement(self):
        if self.measurements is None or len(self.measurements) == 0:
            return None
        return max(self.measurements)

            

if __name__ == "__main__":
    sensor1 = temperatureSensor("TempSensorA", "TS1001", 2018)
    sensor1.printInfo()
    print(f"Sensor Age: {sensor1.getAge()} years")
    sensor2 = temperatureSensor("TempSensorB", "TS1002", 2020)
    sensor2.printInfo()
    print(f"Sensor Age: {sensor2.getAge()} years")# Simulate reading a value from the sensor

    # sensor1.appendToFile(input("Enter the filename to append sensor 1 data: "))
    sensor2.appendToFile()
    print(f"Sensor 1 Calibrated: {sensor1.isCalibrated()}")
    # sensor1.writeToFile(input("Enter the filename to write sensor 1 data (this will overwrite the file): "))
    sensor1.writeToFile("lololol")

    sensor3 = temperatureSensor("", "", 0)
    sensor3.readFromFile("lololol")
    sensor3.printInfo()