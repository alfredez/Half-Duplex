import serial
import time

COM = "/dev/ttyUSB1"
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
        #ser.write("!xxBBM,1,1,0,1,8,83`l7@i@PU>0U>061@E=B0lE=<4LD,4*49".encode("utf-8"))
        #ser.write("!AIBBM,1,1,0,2,14,D89CP9CP1PD5CDP=5CC175,4*5A".encode("utf-8"))
        #ser.write("!xxBBM,1,1,0,1,8,E4Q9Dj19Dj1185A5Dm@PCDECDl57A@,4*17".encode("utf-8"))
        ser.write("!xxBBM,1,1,0,1,8,8211@ldr=SHdDU=CBC`j;5=>DS`i<S8,2*38".encode("utf-8"))

        time.sleep(10)
        # ser_bytes = ser.readline()
        # print(ser_bytes)
    except:
        print("Keyboard Interrupt")
        break
