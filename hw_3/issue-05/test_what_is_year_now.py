import pytest
import what_is_year_now
from unittest.mock import patch, MagicMock


@patch('urllib.request.urlopen')
def test_ok_first_format(mock_urlopen):
    cm = MagicMock()
    cm.getcode.return_value = 200
    cm.read.return_value = \
        '{' \
        '"$id":"1",' \
        '"currentDateTime":"2016-01-01T08:36Z",' \
        '"utcOffset":"00:00:00",' \
        '"isDayLightSavingsTime":false,' \
        '"dayOfTheWeek":"Sunday",' \
        '"timeZoneName":"UTC",' \
        '"currentFileTime":132607893986339880,' \
        '"ordinalDate":"2016-01",' \
        '"serviceResponse":null' \
        '}'
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm

    year = what_is_year_now.what_is_year_now()
    assert year == 2016


@patch('urllib.request.urlopen')
def test_ok_second_format(mock_urlopen):
    cm = MagicMock()
    cm.getcode.return_value = 200
    cm.read.return_value = \
        '{' \
        '"$id":"1",' \
        '"currentDateTime":"01.01.2016T08:36Z",' \
        '"utcOffset":"00:00:00",' \
        '"isDayLightSavingsTime":false,' \
        '"dayOfTheWeek":"Sunday",' \
        '"timeZoneName":"UTC",' \
        '"currentFileTime":132607893986339880,' \
        '"ordinalDate":"2016-01",' \
        '"serviceResponse":null' \
        '}'
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm

    year = what_is_year_now.what_is_year_now()
    assert year == 2016


@patch('urllib.request.urlopen')
def test_fail_invalid_format(mock_urlopen):
    cm = MagicMock()
    cm.getcode.return_value = 200
    cm.read.return_value = \
        '{' \
        '"$id":"1",' \
        '"currentDateTime":"01.2016T08:36Z",' \
        '"utcOffset":"00:00:00",' \
        '"isDayLightSavingsTime":false,' \
        '"dayOfTheWeek":"Sunday",' \
        '"timeZoneName":"UTC",' \
        '"currentFileTime":132607893986339880,' \
        '"ordinalDate":"2016-01",' \
        '"serviceResponse":null' \
        '}'
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm

    with pytest.raises(ValueError):
        what_is_year_now.what_is_year_now()
