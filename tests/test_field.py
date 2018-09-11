from pyfield.field import Field


def test_field():
    field = Field('just a field',
                  default=56,
                  transformator=[str])

    assert field.get == '56'

    field(34)
    assert field.get == '34'

    field('string')
    assert field.get == 'string'

    assert field.prompt_input() == ' just a field [56]: '

    field.default = None
    assert field.prompt_input() == ' just a field: '
