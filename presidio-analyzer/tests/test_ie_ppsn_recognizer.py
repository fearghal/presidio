import pytest

from tests import assert_result
from presidio_analyzer.predefined_recognizers import IePpsnRecognizer


@pytest.fixture(scope="module")
def recognizer():
    return IePpsnRecognizer()


@pytest.fixture(scope="module")
def entities():
    return ["IE_PPS_NUMBER"]


@pytest.mark.parametrize(
    "text, expected_len, expected_positions, expected_score",
    [
        # Valid PPS Numbers
        ("0892727A", 1, ((0, 8),), 1.0),
        ("0892727AB", 1, ((0, 9),), 1.0),
        # Invalid PPS Numbers
        ("089272AB", 0, (), -1.0),
        ("0892727ABC", 0, (), -1.0),
        ("A0892727A", 0, (), -1.0),
        ("421042111", 0, (), -1.0),
        ("1234-0000-0", 0, (), -1.0),
    ],
)
def test_ie_pps_numbers(
    text, expected_len, expected_positions, expected_score, recognizer, entities
):
    results = recognizer.analyze(text, entities)
    assert len(results) == expected_len
    for res, (st_pos, fn_pos) in zip(results, expected_positions):
        assert_result(res, entities[0], st_pos, fn_pos, expected_score)
