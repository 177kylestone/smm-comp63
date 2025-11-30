from smm.calibrate import raw_to_vwc

def test_mid_raw():
    assert abs(raw_to_vwc(511) - 0.25) < 0.02

def test_zero_raw():
    assert raw_to_vwc(0) == 0.0

def test_max_raw():
    assert raw_to_vwc(1023) == 0.5

def test_raw_non_numeric_raises():
    import pytest
    with pytest.raises(ValueError):
        raw_to_vwc('not-a-number')
