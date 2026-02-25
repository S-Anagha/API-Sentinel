DEFAULT_TIMEOUT = 5
RATE_LIMIT_REQUESTS = 25

INJECTION_PAYLOADS = [
    "' OR 1=1 --",
    "\" OR \"1\"=\"1",
    "<script>alert(1)</script>",
    {"$ne": None}
]