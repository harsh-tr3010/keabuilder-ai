def recommend_funnel(industry):
    mapping = {
        "Real Estate": "Lead Form Funnel",
        "Fitness": "Transformation Funnel",
        "Ecommerce": "Product Launch Funnel"
    }
    return mapping.get(industry, "Standard Conversion Funnel")