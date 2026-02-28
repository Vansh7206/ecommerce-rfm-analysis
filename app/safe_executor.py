import re

FORBIDDEN_PATTERNS = [
    r"import ",
    r"os\.",
    r"sys\.",
    r"subprocess",
    r"open\(",
    r"exec\(",
    r"eval\(",
    r"__",
]


def is_code_safe(code: str) -> bool:
    for pattern in FORBIDDEN_PATTERNS:
        if re.search(pattern, code):
            return False
    return True


def execute_code(code: str, df):
    if not is_code_safe(code):
        raise ValueError("Unsafe code detected.")

    # Restrict available globals
    allowed_globals = {
        "df": df
    }

    return eval(code, allowed_globals)