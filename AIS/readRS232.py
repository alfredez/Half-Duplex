import serial
ser = serial.Serial(
    port="COM4", baudrate=38400, bytesize=8, stopbits=serial.STOPBITS_ONE
)
ser.flushInput()

print("Serial is open: " + str(ser.isOpen()))
print("Now Writing")
ser.write("This is a test".encode())
print("Did write, now read")
x = ser.readline()
print(x)

while True:
    try:
        ser_bytes = ser.readline()
        print(ser_bytes)
    except:
        print("Keyboard Interrupt")
        break