def get_options_ratio(option,total):
    if total == 0:
        raise ValueError("Total cannot be zero.")
    return option / total

def get_faculty_rating(ratio):
    if ratio >= 0.9 and ratio < 1:
        return "Excellent"
    elif ratio > 0.8:
        return "Very Good"
    elif ratio > 0.7:
        return "Good"
    elif ratio > 0.6:
        return "Needs Improvement"
    else:
        return "Unacceptable"