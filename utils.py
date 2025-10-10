def normalize_date_range(date_range: str) -> str:
    # Replace any dash (including en dash/em dash) with a normal hyphen
    date_range = date_range.replace("–", "-").replace("—", "-")
    # Remove dots and spaces
    date_range = date_range.replace(".", "").replace(" ", "")
    return date_range
