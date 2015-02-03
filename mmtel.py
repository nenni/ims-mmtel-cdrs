#!/usb/bin/python

from pyasn1.codec.ber import encoder, decoder

from modules import mmtel3gpp32298 as mmtel
from time import sleep

'''
Test to encode and decoder IMS MMTel CDR ber files
'''


def encode_pdu():
    pdu = mmtel.MMTelRecord()
    # print "Strt of cdr log"
    pdu.setComponentByPosition(0, mmtel.RecordType(83), '')
    pdu.setComponentByPosition(2, mmtel.SIPMethod('INVITE'), '')
    pdu.setComponentByPosition(3, mmtel.RoleOfNode(1), '')
    # print pdu
    # print "End of cdr log"
    w_data = encoder.encode(pdu)
    return w_data


def cdr_write(file):
    print "Filename: " + file
    with open(file, 'a+b') as f:
        f.write(encode_pdu())
        f.close


def cdr_read(file):
    f = open(file, 'rb')
    r_data = ''
    while True:
        r_data += f.read()
        # f.close()
        # print r_data
        if not r_data:
            break
        decoder.decode.defaultErrorState = decoder.stDumpRawValue
        pdu = mmtel.MMTelRecord()
        pdu, r_data = decoder.decode(r_data, asn1Spec=pdu)
        for i in range(0,4):
            print pdu.getNameByPosition(i) + ":"  + str(pdu.getComponentByPosition(i)) + ",",
        print "\n"

    f.close()
    # print "data: " + str(data[0])

    # for i in range(0,4):
    # print (pdu.getNameByPosition(i)),
    #     print (pdu.getComponentByPosition(i))

if __name__ == "__main__":
    file = 'mcdr8.ber'
    cdr_write(file)
    # cdr_write(file)

    # sleep(2)
    cdr_read(file)







