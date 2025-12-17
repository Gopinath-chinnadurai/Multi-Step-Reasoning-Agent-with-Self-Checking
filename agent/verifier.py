def verifier(solution: dict):
    """
    Verify the solution:
    - raw_value exists and is numeric
    - non-negative for arithmetic / slots
    """
    checks = []
    raw_value = solution.get("raw_value")

    # Basic numeric validation
    if raw_value is not None and isinstance(raw_value, (int, float)) and raw_value >= 0:
        checks.append({
            "check_name": "basic_validation",
            "passed": True,
            "details": f"Raw value = {raw_value}"
        })
        return {"passed": True, "checks": checks}

    # Failed verification
    checks.append({
        "check_name": "basic_validation",
        "passed": False,
        "details": "Invalid or missing result"
    })
    return {"passed": False, "checks": checks}
