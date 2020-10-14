import pytest

@pytest.fixture()
def setup():
	print("Once before every method.")

def method_A(setup):
	print("From A")

def method_B(setup):
	print("From B")