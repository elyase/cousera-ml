import submit
import os

def test_submit():
    assert True


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
        # set with "export COURSERA_EMAIL='your@email.com'" in bash
    email = os.environ.get("COURSERA_EMAIL", '')
    assert submit.getChallenge(email, 1)[0] == email


def test_output():
    assert len(submit.output(1)) == 200  # value taken from Matlab version
