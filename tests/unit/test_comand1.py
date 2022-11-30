from test_code_cov.commands import comand1

def test_add():
    assert 3 == comand1.add(1, 2)

# def test_sub_div():
#     assert 2 == comand1.sub_div(3, 1)