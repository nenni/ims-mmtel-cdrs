
__author__ = 'nenni'

from pyasn1.type import univ, namedtype, tag, char, namedval, constraint

'''
test to encode and decoder IMS MMTel CDR ber files

Using just a subset of MMTelRecord ASN1 definition defined in 3GPP TS 32.298

DEFINITIONS IMPLICIT TAGS ::=
BEGIN
-- EXPORTS everything
MMTelRecord ::= SET
{
	recordType 							[0] RecordType,
	retransmission						[1] NULL OPTIONAL,
	sIP-Method 							[2] SIP-Method OPTIONAL,
	role-of-Node 						[3] Role-of-Node OPTIONAL,
}

RecordType ::= INTEGER
{
--  Record Value 83 is MMTel specific.
--  The contents are defined in TS 32.275 [35]
--
	mMTelRecord			(83)
}

SIP-Method ::= GraphicString

Role-of-Node ::= ENUMERATED
{
originating (0),
terminating (1)
}

'''


class RecordType(univ.Integer):
    pass


class SIPMethod(char.GraphicString):
    pass


class RoleOfNode(univ.Enumerated):
    namedValues = namedval.NamedValues(
        ('originating', 0),
        ('terminating', 1)
    )
    subtypeSpec = univ.Enumerated.subtypeSpec + constraint.SingleValueConstraint(0, 1)


class MMTelRecord(univ.Set):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('recordType',
                            RecordType().subtype(implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.OptionalNamedType('retransmission', univ.Null().subtype(
            implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.OptionalNamedType('sIP-Method',
                                    SIPMethod().subtype(
                                        implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
        namedtype.OptionalNamedType('role-of-Node',
                                    RoleOfNode().subtype(
                                        implicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
    )


class MMTelRecords(univ.SetOf):
    componentType = MMTelRecord()


if __name__ == "__main__":
    # data = MMTelRecord()
    # data.setComponentByPosition(0, 83)
    # data.setComponentByPosition(2, 'INVITE')
    # data.setComponentByPosition(3, 'originating')
    # print data
    # print (data.prettyPrint())

    records = MMTelRecords()
    record = MMTelRecord()

    records.setComponentByPosition(0, record.setComponentByPosition(0, RecordType(83), '')),
    records.setComponentByPosition(0, record.setComponentByPosition(2, SIPMethod('INVITE'), ''))
    records.setComponentByPosition(0, record.setComponentByPosition(3, RoleOfNode('originating'), ''))

    print record.prettyPrint()
    print records.prettyPrint()










