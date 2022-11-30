from test_code_cov.commands import comand1
from test_code_cov.commands import comand2
def test_add():
    assert 3 == comand1.add(1, 2)

def test_sub_div():
    print(comand1.sub_div(3, 1))
    assert 2, 8 == comand1.sub_div(3, 1)

def test_com2():
    assert 2 == comand2.power(2, 1)
