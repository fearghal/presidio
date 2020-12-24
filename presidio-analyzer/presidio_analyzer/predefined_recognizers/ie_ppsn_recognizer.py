from presidio_analyzer import Pattern, PatternRecognizer


class IePpsnRecognizer(PatternRecognizer):
    """
    Recognizes Irish PPS number.
    This is the Irish government's "personal public service number".
    A PPS Number is always 7 numbers followed by either one or two letters.
    https://www.gov.ie/en/service/12e6de-get-a-personal-public-service-pps-number
    """

    PATTERNS = [
        Pattern("Irish PPS number", r"\b\d{7}[a-zA-Z]{1,2}\b", 1.0,),
    ]

    CONTEXT = [
        "ppsn",
        "pps number",
    ]

    def __init__(
        self,
        patterns=None,
        context=None,
        supported_language="en",
        supported_entity="IE_PPS_NUMBER",
        replacement_pairs=None,
    ):
        self.replacement_pairs = replacement_pairs or [("-", "")]
        patterns = patterns if patterns else self.PATTERNS
        context = context if context else self.CONTEXT
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            context=context,
            supported_language=supported_language,
        )
