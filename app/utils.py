def get_recycling_tip(waste_type):
    tips = {
        "Plastic": "Place in recycling bin.",
        "Paper": "Recycle with paper products.",
        "Glass": "Clean before recycling.",
        "Metal": "Recycle at metal collection center.",
        "Organic": "Use for composting."
    }

    return tips.get(waste_type, "No recommendation available.")