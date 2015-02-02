#!/usb/bin/python

from modules import mmtel3gpp32298 as mmtel
from pyasn1.codec.ber import encoder, decoder

'''
Test to encode and decoder IMS MMTel CDR ber files
Using just a subset of MMTelRecord ASN1 definition defined in 3GPP TS 32.298
'''


def cdr_write(file):
    records = mmtel.MMTelRecords()
    record = mmtel.MMTelRecord()


    records.setComponentByPosition(1, record.setComponentByPosition(0, mmtel.RecordType(83), ''))
    records.setComponentByPosition(1, record.setComponentByPosition(2, mmtel.SIPMethod('INVITE'), ''))
    records.setComponentByPosition(1, record.setComponentByPosition(3, mmtel.RoleOfNode('originating'), ''))

    print record.prettyPrint()
    print records.prettyPrint()

    w_data = encoder.encode(records)
    print w_data

    print "Filename: " + file
    with open(file, 'wb') as f:
        f.write(w_data)
        f.close


def cdr_read(file):
    print "Filename: " + file
    with open(file, 'rb') as f:
        rdata = f.read()
        # f.close
        rdata = decoder.decode(mmtel.MMTelRecords.prettyPrint())


if __name__ == "__main__":
    cdr_write('mcdr1.ber')








