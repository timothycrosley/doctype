from examples import example, verify_and_test_examples

from doctype import Doc
from typing_extensions import Literal


def test_doc():
    @example(1, 1)
    def add(
        number_1: Doc[int, Literal["First number"]], number_2: Doc[int, Literal["Second number"]]
    ) -> Doc[int, Literal["Both numbers added together"]]:
        return number_1 + number_2

    verify_and_test_examples(add)
