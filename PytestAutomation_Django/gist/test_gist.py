import pytest

def test_our_first_test() -> None:
    assert 1 == 1


# if we want to skip a test...
@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2

# conditional skip
@pytest.mark.skipif(4 > 1, reason="Because 4 > 1")
def test_should_be_skipped_if() -> None:
    assert 1 == 2

# we know it will fail but want to run test anyway. output is XFAIL if fails, XPASS if passes.
@pytest.mark.xfail
def test_dont_care_if_fails() -> None:
    assert 1 == 2

# custom marker. Really, we should document this in pytest.ini configuration file
@pytest.mark.slow
def test_with_custom_mark() -> None:
    pass
