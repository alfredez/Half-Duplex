import serial
ser = serial.Serial(
    port="COM4", baudrate=38400, bytesize=8, stopbits=serial.STOPBITS_ONE
)
ser.flushInput()

while True:
    try:
        ser_bytes = ser.readline()
        print(ser_bytes)
    except:
        print("Keyboard Interrupt")
        break