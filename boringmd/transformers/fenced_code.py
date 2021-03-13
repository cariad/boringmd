from typing import Optional

from lstr import lstr

from boringmd.line_guidance import LineGuidance
from boringmd.transformers.transformer import Transformer


class FencedCodeTransformer(Transformer):
    """ Removes fences from fenced code. """

    def __init__(self) -> None:
        self.inside = False

    def transform(self, line_number: int, line: lstr) -> Optional[LineGuidance]:
        """
        Removes fences from fenced code.

        Arguments:
            line_number: Line number of the source document.
            Line:        Line to transform.

        Returns:
            Guidance (if any) for further transformation.
        """

        if str(line).startswith("```"):
            self.inside = not self.inside
            return LineGuidance(delete=True)

        if self.inside:
            return LineGuidance(stop=True)

        return None
