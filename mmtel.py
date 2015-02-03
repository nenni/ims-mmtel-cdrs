#!/usb/bin/python

from pyasn1.codec.ber import encoder, decoder

from modules import mmtel3gpp32298 as mmtel

from time import sleep


'''
Test to encode and decoder IMS MMTel CDR ber files
Using just a subset of MMTelRecord ASN1 definition defined in 3GPP TS 32.298
'''

def encode_pdu():
        pdu = mmtel.MMTelRecord()
        print "Strt of cdr log"
        pdu.setComponentByPosition(0, mmtel.RecordType(83), '')
        pdu.setComponentByPosition(2, mmtel.SIPMethod('INVITE'), '')
        pdu.setComponentByPosition(3, mmtel.RoleOfNode(0), '')
        print pdu
        print "End of cdr log"
        w_data = encoder.encode(pdu)
        return w_data


def cdr_write(file):
    print "Filename: " + file
    with open(file, 'a+b') as f:
        f.write(encode_pdu())
        f.close


def cdr_read(file):
    with open(file, 'rb') as f:
        r_data = f.read
        f.close()
        decoder.decode.defaultErrorState = decoder.stDumpRawValue
        data = decoder.decode(r_data, asn1Spec=mmtel.MMTelRecord)
        print data


if __name__ == "__main__":

    file = 'mcdrtagclassapp4.ber'
    cdr_write(file)
    # cdr_write(file)
    # cdr_read(file)







