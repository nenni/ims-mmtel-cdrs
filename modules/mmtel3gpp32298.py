__author__ = 'nnenchev'

from pyasn1.type import univ, namedtype, tag, char, namedval, constraint


'''
Test to encode and decoder IMS MMTel CDR ber files
Using just a subset of MMTelRecord ASN1 definition defined in 3GPP TS 32.298
'''

MAX = 64

class RecordType(univ.Integer):
    namedValues = namedval.NamedValues(
        ('mMTelRecord', 83)
    )


class SIPMethod(char.GraphicString): pass


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
    sizeSpec = univ.SetOf.sizeSpec + constraint.ValueSizeConstraint(1, MAX)


class MMTelRecords(univ.SetOf):
    componentType = MMTelRecord()
    sizeSpec = univ.SetOf.sizeSpec + constraint.ValueSizeConstraint(1, MAX)
