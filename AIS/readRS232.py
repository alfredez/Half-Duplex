import serial
import time

DOS_EOL = "\x0D\x0A"
'''
DOS style end-of-line (<cr><lf>) for talking to AIS base stations
'''
EOL=DOS_EOL

COM = "COM12"
ser = serial.Serial(
    port=COM, baudrate=38400, bytesize=8, stopbits=serial.STOPBITS_ONE
)
ser.flushInput()

print("Serial is open: " + str(ser.isOpen()))
print("Now Writing")
#ser.write("!AIABM,1,1,0,244123459,3,6,6te@PU>0U>061@E=B0lE=<4LD,4*13".encode("utf-8"))
#ser.write(b'00000000010010100100100101110100111011010000110010010101101000000101000010000010010100111000000010010100111000000000011000000101000001010100110101001000000011010001010100110100110000010001110001')
#ser.write(b'00000000010010100100100101110100111011010000110010010101101000000101000010000010010100111000000010010100111000000000011000000101000001010100110101001000000011010001010100110100110000010001110001')

# print("Did write, now read")
# x = ser.readline()
# print(x)
print("Now starting loop")
while True:
    try:
        print("Writing to " + COM)
        #ser.write(b'00000000010010100100100101110100111011010000110010010101101000000101000010000010010100111000000010010100111000000000011000000101000001010100110101001000000011010001010100110100110000010001110001')
        #ser.write("!AIBBM,1,1,0,0,8,04a@PU>0U>061@E=B0lE=<4LD,4*49"+EOL)
        #ser.write("!AIBBM,1,1,0,2,8,04a9M>1@PU>0U>061@E=@,4*16".encode("utf-8"))
        #ser.write("!AIBBM,1,1,0,2,8,04a9M>1@PU>0U>06185=08E99V1@E=4,0*7C".encode("utf-8"))
        ser.write("!xxBBM,1,1,0,1,8,E4Q9Dj19Dj1185A5Dm@PCDE,0*7B".encode("utf-8"))


        time.sleep(10)
        # ser_bytes = ser.readline()
        # print(ser_bytes)
    except:
        print("Keyboard Interrupt")
        break