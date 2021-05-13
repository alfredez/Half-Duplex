import serial
import time

COM = "/dev/ttyUSB0"
ser = serial.Serial(
    port=COM, baudrate=38400, bytesize=8, stopbits=serial.STOPBITS_ONE
)
ser.flushInput()

print("Serial is open: " + str(ser.isOpen()))

print("Now starting loop")
while True:
    try:
        print("Writing to " + COM)
        #ser.write("!AIBBM,1,1,0,2,8,04a9M>1@PU>0U>061@E=@,4*16".encode("utf-8"))
        #ser.write("!AIBBM,1,1,0,2,8,04a9M>1@PU>0U>06185=08E99V1@E=4,0*7C".encode("utf-8"))
        ser.write("!xxBBM,1,1,0,1,8,E4Q9Dj19Dj1185A5Dm@PCDE,0*7B".encode("utf-8"))

        time.sleep(10)
        # ser_bytes = ser.readline()
        # print(ser_bytes)
    except:
        print("Keyboard Interrupt")
        break
