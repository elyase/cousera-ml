import submit


def test_submit():
    assert len(submit.validParts) == len(submit.sources)


def test_bitadd():
    assert submit.bitadd(64, 2*2*2*2*2) == 96
    assert submit.bitadd(100000000000, -123) == 4294967295


def test_sha1():
    assert submit.sha1('abcd') == '81fe8bfe87576c3ecb22426f8e57847382917acf'  # Value taken from from Matlab version


def test_base64encode():
    warm_up_result = """1.00000 0.00000 0.00000 0.00000 0.00000 0.00000 1.00000 0.00000 0.00000 0.00000 0.00000 0.00000 1.00000 0.00000 0.00000 0.00000 0.00000 0.00000 1.00000 0.00000 0.00000 0.00000 0.00000 0.00000 1.00000 """
    warm_up_matlab_encoded = """MS4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMC4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMS4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMC4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMS4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMC4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMS4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMC4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMS4wMDAwMCA="""
    assert submit.base64encode(warm_up_result) == warm_up_matlab_encoded
