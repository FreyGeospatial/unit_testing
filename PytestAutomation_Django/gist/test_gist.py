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

def test_blah() -> None:
    print("blah")

def test_blah2() -> None:
    return "blah"

class Company:
    def __init__(self, name: str, stock_symbol: str):
        self.name = name,
        self.stock_symbol = stock_symbol
    
    def __str__(self):
        return f"{self.name}:{self.stock_symbol}"

# a fixture is a function that we can use to return anything we want. By
# marking this function as a fixture, we are telling PyTest that we may 
# run this before or after our TEST FUNCTIONS  . Can also pass fixtures into other
# functions.
@pytest.fixture
def company() -> Company: # type annotations...returns a company instance
    return Company(name="Fiver", stock_symbol="FVRR") # returns a company instance with name and stock symbol

# if pytest finds a FIXTURE^^^ with the matching name of an argument to send to a function (below), 
# Pytest will execute that function before(?) and puts the output of that function as the argument 
# for the test function(?)
def test_with_ficture(company: Company) -> None: # type annotations...returns None type. Takes a company fixture/instance 
    print(f"printing {company} from fixture")
    
# run $ pytest . -v for verbose terminal output (which test files and test functions are being run)
# run $ pytest . -v no:warnings to remove warnings from terminal output
# run $ pytest . -v no:warnings -s to also print the test function output

# parametrization allows us to pass variable inputs to test functions
@pytest.mark.parametrize(
    "company_name", # the first thing we want to do is supply variable arguments to the "comapny_name" parameter
    ["TikTok", "Instagram", "Twitch"], # these are the variable inputs we will supply... so there will be 3 test runs of this function
    ids=["TIKTOK TEST", "INSTAGRAM TEST", "TWITCH TEST"] # optional labels for input
)

# ** note that the name of the parametrize marker above^^^ is the same as the parameter for the tested function below
def test_parametrized(company_name:str) -> None:
    print(f"\nTest with {company_name}")
