'''
Interfacing of GPS module with system using python script.
'''
import serial
import re
import time 
Serial_Port = 'COM21'
Baudrate = 9600


def extractLocation(gps_str):
    ''' This function extract gps location information.'''
    gps_info = dict()
    if  re.search('GPGGA',gps_str):
        #print(str)
        gps_str= gps_str.split(',')
        timestamp = gps_str[1][0:2]+":"+gps_str[1][2:4]+":"+gps_str[1][4:6]+""+"+00:00"
        gps_info.update({"timestamp": timestamp, 
                         "latitude" : gps_str[2], 
                         "latitude_dir" : gps_str[3],
                         "longitude" : gps_str[4],
                         "longitude_dir" : gps_str[5],
                         "altitude" : gps_str[9],
                         "altitude_units" :  gps_str[10] 
                         })
        #print("Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s" %
        #     (gps_info["timestamp"], gps_info["latitude"], gps_info["latitude_dir"], 
        #      gps_info["longitude"], gps_info["longitude_dir"],gps_info["altitude"], 
        #      gps_info["altitude_units"]))
        return gps_info

def main():
    try:
        serialPort = serial.Serial(Serial_Port , Baudrate , timeout = 0.5)
        while True:
            gps_str = serialPort.readline().decode('utf-8', errors='ignore').strip()
            #print(gps_str)
            gps_info = extractLocation(gps_str)
            #print(gps_info)
            if gps_info != None:
                  print("Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s" %
                  (gps_info["timestamp"], gps_info["latitude"], gps_info["latitude_dir"], 
                  gps_info["longitude"], gps_info["longitude_dir"],gps_info["altitude"], 
                  gps_info["altitude_units"]))
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("Execution Stopped by User")
         
if __name__ =='__main__':
    main()