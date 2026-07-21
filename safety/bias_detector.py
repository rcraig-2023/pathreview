"""Bias detection in generated feedback."""

import re

import structlog

logger = structlog.get_logger()


class BiasDetector:
    """Detect biased language in feedback."""

    # Genuinely dismissive phrases about educational background
    DISMISSIVE_PATTERNS = [
        # "bootcamp/self-taught/online course education/training is insufficient/inadequate"
        r"(?:bootcamp|self-taught|online\s+course)\s+(?:education|training)\s+is\s+(?:insufficient|inadequate|lacks)",
        # "bootcamp education lacks fundamentals"
        r"(?:bootcamp|self-taught|online\s+course)\s+(?:education|training)\s+lacks",
        # "bootcamp graduates/developers/programmers lack/missing rigor/fundamentals"
        r"(?:bootcamp|self-taught)\s+(?:graduates?|developers?|programmers?)\s+(?:lack|missing)\s+(?:rigor|fundamentals|proper\s+training)",
        # "bootcamp/coding bootcamp graduates/developers/programmers can't/cannot/won't"
        r"(?:coding\s+bootcamp|bootcamp)\s+(?:graduates?|developers?|programmers?)\s+(?:can't|cannot|won't|will\s+not)",
        # "bootcamp doesn't/does not prepare you/developers"
        r"(?:bootcamp|coding\s+bootcamp)\s+(?:doesn't|does\s+not)\s+prepare\s+(?:you|developers?)",
        # "self-taught/bootcamp is not/never equal/comparable to university"
        r"(?:self-taught|bootcamp)\s+is\s+(?:not|never)\s+(?:equal|comparable)\s+to\s+(?:university|traditional|formal)",
        # "self-taught/bootcamp developers are not equal/comparable to ..."
        r"(?:self-taught|bootcamp)\s+developers?\s+are\s+not\s+(?:equal|comparable)\s+to",
        # "bootcamp attendance means inadequate/insufficient training"
        r"(?:bootcamp|self-taught)\s+\w+\s+means\s+(?:inadequate|insufficient|lacking)",
    ]

    # Demographic assumptions (about age, background, identity)
    DEMOGRAPHIC_PATTERNS = [
        # "young/old/aged person/developer/programmer can't/cannot/won't/will not ..."
        r"(?:young|old|aged)\s+(?:person|developers?|programmers?)\s+(?:can't|cannot|won't|will\s+not)",
        # "person from / coming from poor/rich/working class"
        r"(?:person\s+from|coming\s+from)\s+(?:poor|rich|working[\s-]?class)",
        # "developers from poor/rich/working-class backgrounds can't ..."
        r"developers?\s+from\s+(?:poor|rich|working[\s-]?class)\s+backgrounds?\s+(?:can't|cannot|won't|will\s+not)",
        # "immigrant/international/foreign developers can't/cannot/won't/struggle"
        r"(?:immigrant|international|foreign)\s+developers?.*(?:can't|cannot|won't|struggle)",
    ]

    @staticmethod
    def detect_bias(text: str) -> tuple[bool, str]:
        """Detect biased language in feedback.

        Args:
            text: Feedback text

        Returns:
            Tuple of (is_biased, reason)
        """
        # Check for dismissive language about education
        for pattern in BiasDetector.DISMISSIVE_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE):
                reason = "Dismissive language about educational background"
                logger.warning("bias_detected", reason=reason)
                return True, reason

        # Check for demographic assumptions
        for pattern in BiasDetector.DEMOGRAPHIC_PATTERNS:
            if re.search(pattern, text, re.IGNORECASE):
                reason = "Demographic assumptions detected"
                logger.warning("bias_detected", reason=reason)
                return True, reason

        return False, ""
