import pytest
import morse


@pytest.mark.parametrize('test_input, expected', [
    ('... --- ...', 'SOS'),
    ('---', 'O'),
    ('.-.. --- -. --. .-- --- .-. -..', 'LONGWORD')
])
def test_decode(test_input, expected):
    assert morse.decode(test_input) == expected
