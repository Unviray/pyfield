from pyfield.field import Field


def test_field():
    field = Field('just a field',
                  transformator=[str])

    field('string')
    assert field.get == 'string'

    field(34)
    assert field.get == '34'
