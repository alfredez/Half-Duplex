import sys
from decimal import Decimal

import bitstring
from BitVector import BitVector
from aisutils import aisstring
from aisutils import binary
from aisutils import uscg


def checksumStr(data, verbose=False):
    end = data.find('*')  # FIX: would rfind be faster?
    start = 0
    if data[0] in ('$', '!'): start = 1
    if -1 != end:
        data = data[start:end]
    else:
        data = data[start:]
    if verbose: print
    'checking on:', start, end, data
    # FIX: rename sum to not shadown builting function
    sum = 0
    for c in data: sum = sum ^ ord(c)
    sumHex = "%x" % sum
    if len(sumHex) == 1: sumHex = '0' + sumHex
    return sumHex.upper()


def bbmEncode(totSent, sentNum, seqId, aisChan, msgId, data, numFillBits
              , prefix='xx', appendEOL=True
              , validate=True
              ):
    if validate:
        tot = int(totSent)
        assert (0 < tot and tot <= 9)
        num = int(sentNum)
        assert (0 < num and num <= 9)
        assert (num <= tot)

        seq = int(seqId)

        assert (0 <= seq and seq <= 9)

        assert (int(aisChan) in range(0, 5))

        assert (int(msgId) in (8, 14))
        assert (int(numFillBits) in range(0, 6))

        r = ','.join(
            ('!' + prefix + 'BBM', str(totSent), str(sentNum), str(seqId), str(aisChan), str(msgId), data, str(numFillBits)))

        r += '*' + checksumStr(r)

        if validate: assert (len(r)) <= 81  # Max nmea string length

        return r



def encode_BBM(params):
    '''Create a bin_broadcast binary message payload to pack into an AIS Msg bin_broadcast.

    Fields in params:
      - MessageID(uint): AIS message number.  Must be 8 (field automatically set to "8")
      - RepeatIndicator(uint): Indicated how many times a message has been repeated
      - UserID(uint): Unique ship identification number (MMSI)
      - Spare(uint): Reserved for definition by a regional authority. (field automatically set to "0")
      - dac(uint): Appid designated area code (country)
      - fi(uint): Appid functional identifier
      - BinaryData(binary): Bits for a binary broadcast message
    @param params: Dictionary of field names/values.  Throws a ValueError exception if required is missing
    @param validate: Set to true to cause checking to occur.  Runs slower.  FIX: not implemented.
    @rtype: BitVector
    @return: encoded binary message (for binary messages, this needs to be wrapped in a msg 8
    @note: The returned bits may not be 6 bit aligned.  It is up to you to pad out the bits.
    '''

    bvList = []
    bvList.append(binary.setBitVectorSize(BitVector(intVal=8), 6))
    if 'RepeatIndicator' in params:
        bvList.append(binary.setBitVectorSize(BitVector(intVal=params['RepeatIndicator']), 2))
    else:
        bvList.append(binary.setBitVectorSize(BitVector(intVal=0), 2))
    bvList.append(binary.setBitVectorSize(BitVector(intVal=params['UserID']), 30))
    bvList.append(binary.setBitVectorSize(BitVector(intVal=0), 2))
    bvList.append(binary.setBitVectorSize(BitVector(intVal=params['dac']), 10))
    bvList.append(binary.setBitVectorSize(BitVector(intVal=params['fi']), 6))
    bvList.append(params['BinaryData'])

    return binary.joinBV(bvList)


def testParams():
    '''Return a params file base on the testvalue tags.
    @rtype: dict
    @return: params based on testvalue tags
    '''

    params = {}
    params['MessageID'] = 8
    params['RepeatIndicator'] = 1
    params['UserID'] = 1193046
    params['Spare'] = 0
    params['dac'] = 366
    params['fi'] = 42
    params['BinaryData'] = BitVector(
        bitstring='110000101100000111100010010101001110111001101010011011111111100000110001011100001011111111101111111110011001000000010001110')

    return params


class Device:
    def __init__(self, name, branch, model, port, type):
        self.name = name
        self.branch = branch
        self.model = model
        self.port = port
        self.binarydata = 0
        self.status = 0
        self.type = 0

    def getname(self):
        print("Wireless device name " + self.name)

    def getport(self):
        print("Wireless device port " + self.port)

    def connect(self):
        print("Wireless device port " + self.port)

    def check_connection(self):
        print("Wireless device port " + self.port)

    def status(self):
        print("Wireless device port " + self.port)

    def transmission(self):
        print("Wireless device port " + self.port)

    def terminate_connection(self):
        print("Wireless device port " + self.port)

    def insert_payload(self):
        print("Wireless device port " + self.port)

    def encode_binarydata(self):
        print("Wireless device port " + self.port)

    def encode_ABM(self):
        print("Wireless device port " + self.port)


# name, branch, model, port, type
p1 = Device("AIS", "True Heading", "AIS Base Station", "COM4", 1)

p1.getname()
msgDict = {
    'MessageID': '8',
    'RepeatIndicator': 0,
    'UserID': 244123459,
    'Spare': '0',
    'dac': 1,
    'fi': 10,
    'BinaryData': BitVector(
        textstring='THIS IS A TEST MESSAGE'),
}


test = encode_BBM(msgDict)
print(BitVector(textstring='THIS IS A TEST MESSAGE'))
print(bbmEncode(1,1,0,1,8,'THIS IS A TEST MESSAGE',0,appendEOL=False))
