from network import LoRa
import machine
import time
import ubinascii
import socket
import struct

def send_data(dev_type):
    #Skicka datan beroende på vilken typ av device som används. För antal platser
    #så används dev_type 1, dvs man skickar i första byten. Används enskilda parkeringar
    #så valde jag att skapa en "Identifier" byte för att vet vilken typ av data man skickar upp
    #den ligger som bytes[0]. Som det är strukturerat nu så är 255 assignat till Enskilda parkeringar
    #och då används bytes[1] och bytes[2] för visualisering.
    if dev_type == 1 or dev_type == 3:
        package = struct.pack('>B',empty_slots)
        s.send(package)
    elif dev_type == 2:
        package_decider = struct.pack('>B', 255)
        package_slot_1 = struct.pack('>B', time_parked['sensor_2']//60)
        package_slot_2 = struct.pack('>B', time_parked['sensor_1']//60)
        s.send(package_decider+package_slot_1+package_slot_2)

def socket_init():
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 0)
    return s

#Pins defining
sensor_1 = machine.Pin("P16", mode = machine.Pin.IN)
sensor_2 = machine.Pin("P15", mode = machine.Pin.IN)
sensor_3 = machine.Pin("P12", mode = machine.Pin.OUT)

#LoRA Connection
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = ubinascii.unhexlify("70B3D57ED0039B74")
app_key = ubinascii.unhexlify("B1E4BAF7B470EC0589D5551332AB2D1E")

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

while not lora.has_joined():
    print("Waiting for acceptance")
    time.sleep(3)

sensor_3.value(1)

#Base values
empty_slots = 50
s = socket_init()
send_data(1)
sensors = {"sensor_1" : sensor_1, "sensor_2" : sensor_2}
time_parked = {"sensor_1" : 0, "sensor_2" : 0}

#Device type: dev_type, 1 = in och ut parkeringshus, 2 = platsparkering, 3 = testning_in_o_ut
dev_type = 2

while True:
    #Checking if the time is divisible by 60, if so then send data to TTN.
    if dev_type == 3:
        if time.time() % 15 == 0:
            send_data(dev_type)

    elif time.time() % 60 == 0:
        send_data(dev_type)

#    if not lora.has_joined():
#        lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
#
#        while not lora.has_joined():
#            print("Waiting for acceptance")
#            time.sleep(3)

    #Checking if sensor 1 is triggered before sensor 2, if so the car is entering the parking space.
    #Only if the car triggers the second sensor in a certain time frame. If the second sensor triggers first, then the car is moving out from the parking slot.
    if dev_type == 1 or dev_type == 3: #In- och utfart.
        if sensor_1.value() == 0:
            time_start = time.time()
            while sensor_1.value() == 0:
                if sensor_2.value() == 0:
                    time_between = time.time() - time_start
                    if not time_between < 1 and not time_between > 2:
                        empty_slots -= 1
                        print(str(empty_slots))
                        time.sleep(1)

        if sensor_2.value() == 0:
            time_start = time.time()
            while sensor_2.value() == 0:
                if sensor_1.value() == 0:
                    time_between = time.time() - time_start
                    if not time_between < 1 and not time_between > 2:
                        if empty_slots != 50:
                            empty_slots += 1
                            print(str(empty_slots))
                            time.sleep(1)

    elif dev_type == 2: #Enskild parkering
        #loops through the sensors, checking if they are active or not
        #updates the time each car has been parked
        for sensor in sensors:
            if sensors[sensor].value() == 0:
                time_parked.update({sensor : time_parked[sensor] + 2})
            elif sensors[sensor].value() == 1:
                time_parked.update({sensor : 0})
        time.sleep(2)
