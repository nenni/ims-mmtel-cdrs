__author__ = 'nnenchev'

from pyasn1.type import univ, namedtype, tag, char, namedval, constraint


'''
Test to encode and decoder IMS MMTel CDR ber files
Using just a subset of MMTelRecord ASN1 definition defined in 3GPP TS 32.298
'''


class RecordType(univ.Integer):
    tagSet = univ.Integer.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatSimple, 0))
    namedValues = namedval.NamedValues(('mMTelRecord', 83))


class SIPMethod(char.GraphicString):
        tagSet = char.GraphicString.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatSimple, 2))


class RoleOfNode(univ.Enumerated):
    tagSet = univ.Enumerated.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatSimple, 3))
    namedValues = namedval.NamedValues(
        ('originating', 0),
        ('terminating', 1)
    )
    subtypeSpec = univ.Enumerated.subtypeSpec + constraint.SingleValueConstraint(0, 1)


class MMTelRecord(univ.Set):
    componentType = namedtype.NamedTypes(
        namedtype.NamedType('recordType', RecordType()),
        namedtype.OptionalNamedType('retransmission', univ.Null()),
        namedtype.OptionalNamedType('sIP-Method', SIPMethod()),
        namedtype.OptionalNamedType('role-of-Node', RoleOfNode()),
    )
