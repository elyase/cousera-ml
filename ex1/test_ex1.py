import submit


def test_submit():
    assert len(submit.validParts) == len(submit.sources)


def test_sha1():
    assert submit.sha1('abcd') == '81fe8bfe87576c3ecb22426f8e57847382917acf'  # Value taken from from Matlab version


def test_base64encode():
    warm_up_result = """1.00000 0.00000 0.00000 0.00000 0.00000 0.00000 1.00000 0.00000 0.00000 0.00000 0.00000 0.00000 1.00000 0.00000 0.00000 0.00000 0.00000 0.00000 1.00000 0.00000 0.00000 0.00000 0.00000 0.00000 1.00000 """
    warm_up_matlab_encoded = """MS4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMC4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMS4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMC4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMS4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMC4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMS4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMC4wMDAwMCAwLjAwMDAwIDAuMDAwMDAgMS4wMDAwMCA="""
    assert submit.base64encode(warm_up_result) == warm_up_matlab_encoded


def test_isValidPartId():
    assert submit.isValidPartId(1)
    assert not submit.isValidPartId(0)
    assert not submit.isValidPartId(9)


def test_getChallenge():
    email = 'yaser.martinez@gmail.com'
    assert submit.getChallenge(email, 1)[0] == email
