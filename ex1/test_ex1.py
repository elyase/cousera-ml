import submit


def test_submit():
    assert len(submit.validParts) == len(submit.sources)
