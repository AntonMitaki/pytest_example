import pytest
from contextlib import nullcontext as does_not_raise

from src.main import MiddleChar, NotAStringError, TooShortError


class TestMiddleChar:
    @pytest.mark.parametrize(
        "word, result, error",
        [
            ('test', 'es', does_not_raise()),
            ('testing', 't', does_not_raise()),
            ('', False, pytest.raises(TooShortError)),
            ('t', False, pytest.raises(TooShortError)),
            ('te', False, pytest.raises(TooShortError)),
            (-1, False, pytest.raises(NotAStringError)),
            (['qwe'], False, pytest.raises(NotAStringError)),
            (1.05, False, pytest.raises(NotAStringError)),
        ]
    )
    def test_middle_char_get(self, word, result, error):
        with error:
            assert MiddleChar.get(word) == result
