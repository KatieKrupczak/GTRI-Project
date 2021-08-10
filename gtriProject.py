#import python libraries
import os, datetime

#import gpiozero libraries for sensors & hardware etc
from gpiozero import PingServer

#identity data like patient name & id
patient_name = "name"
patient_id = "id"
pi_id = "pi_id"

try:
    while True:
    #Save data to file per day
        file_path = "/home/pi/Documents/GTRI-Project" #absolute folder path for txt files holding sensor data

        #get current date
        date_time = datetime.datetime.now()
        print(date_time)

        #get file name and complete file path
        file_name = date_time.strftime('%d-%m-%Y.txt')
        file_path_name = os.path.join(file_path,file_name) #file_path + name for the day's sensor data

        #check if txt file exists for date else create new txt file
        if not (os.path.exists(file_path_name)):
            print("file does not already exist")
            #create txt file
            with open(file_path_name,'w') as file:
                file.write(date_time.strftime('Date: %d-%m-%Y\n'))
                file.write("Patient Name: "+patient_name+'\n')
                file.write("Patient ID: "+patient_id+'\n')
                file.write("Raspberry Pi ID: "+pi_id+'\n\n')
                
                print("file created")
                pass
        
            #Verify File created
            if not(os.path.isfile(file_path_name)):
                raise FileNotFoundError("File %s failed to be created"%file_name)
        else:
            print("File already exists")
        # File exists. Add data

except KeyboardInterrupt:
    exit()