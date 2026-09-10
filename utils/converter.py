# Unit Converter Module
# Uses functions with parameters (from Rubicon Training)


# ============================================================
# CONVERSION DATA
# ============================================================

LENGTH_UNITS = {
    "Meter (m)": 1.0,
    "Kilometer (km)": 1000.0,
    "Centimeter (cm)": 0.01,
    "Millimeter (mm)": 0.001,
    "Mile": 1609.344,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254,
    "Nautical Mile": 1852.0,
}

WEIGHT_UNITS = {
    "Kilogram (kg)": 1.0,
    "Gram (g)": 0.001,
    "Milligram (mg)": 0.000001,
    "Metric Ton": 1000.0,
    "Pound (lb)": 0.453592,
    "Ounce (oz)": 0.0283495,
    "Stone": 6.35029,
}

SPEED_UNITS = {
    "m/s": 1.0,
    "km/h": 0.277778,
    "mph": 0.44704,
    "knot": 0.514444,
    "ft/s": 0.3048,
}

DATA_UNITS = {
    "Bit": 1,
    "Byte": 8,
    "Kilobyte (KB)": 8 * 1024,
    "Megabyte (MB)": 8 * 1024 ** 2,
    "Gigabyte (GB)": 8 * 1024 ** 3,
    "Terabyte (TB)": 8 * 1024 ** 4,
    "Kilobit (Kb)": 1000,
    "Megabit (Mb)": 1000 ** 2,
    "Gigabit (Gb)": 1000 ** 3,
}

AREA_UNITS = {
    "Square Meter (m²)": 1.0,
    "Square Kilometer (km²)": 1e6,
    "Square Centimeter (cm²)": 1e-4,
    "Hectare": 1e4,
    "Acre": 4046.86,
    "Square Foot (ft²)": 0.092903,
    "Square Inch (in²)": 0.00064516,
    "Square Mile": 2.59e6,
}

TIME_UNITS = {
    "Second": 1.0,
    "Millisecond": 0.001,
    "Minute": 60.0,
    "Hour": 3600.0,
    "Day": 86400.0,
    "Week": 604800.0,
    "Month (30 days)": 2592000.0,
    "Year (365 days)": 31536000.0,
}


# ============================================================
# CONVERSION FUNCTIONS
# ============================================================

def convert_unit(value, from_unit, to_unit, unit_dict):
    """Convert between units using a conversion dictionary."""
    if from_unit not in unit_dict or to_unit not in unit_dict:
        return None, "Invalid unit"
    
    # Convert to base unit, then to target
    base_value = value * unit_dict[from_unit]
    result = base_value / unit_dict[to_unit]
    return result, None


def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    # Convert to Celsius first
    if from_unit == "Celsius (°C)":
        celsius = value
    elif from_unit == "Fahrenheit (°F)":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin (K)":
        celsius = value - 273.15
    else:
        return None, "Invalid unit"
    
    # Convert from Celsius to target
    if to_unit == "Celsius (°C)":
        return celsius, None
    elif to_unit == "Fahrenheit (°F)":
        return (celsius * 9 / 5) + 32, None
    elif to_unit == "Kelvin (K)":
        return celsius + 273.15, None
    else:
        return None, "Invalid unit"


# ============================================================
# CATEGORY MAPPING
# ============================================================

CATEGORIES = {
    "📏 Length": LENGTH_UNITS,
    "⚖️ Weight": WEIGHT_UNITS,
    "🌡️ Temperature": None,  # Special handling
    "🏎️ Speed": SPEED_UNITS,
    "💾 Data Storage": DATA_UNITS,
    "📐 Area": AREA_UNITS,
    "⏱️ Time": TIME_UNITS,
}

TEMPERATURE_UNITS = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]


def get_units_for_category(category):
    """Get available units for a category."""
    if category == "🌡️ Temperature":
        return TEMPERATURE_UNITS
    return list(CATEGORIES[category].keys()) if CATEGORIES.get(category) else []


def convert(value, from_unit, to_unit, category):
    """Universal conversion function."""
    if category == "🌡️ Temperature":
        return convert_temperature(value, from_unit, to_unit)
    
    unit_dict = CATEGORIES.get(category)
    if unit_dict is None:
        return None, "Unknown category"
    
    return convert_unit(value, from_unit, to_unit, unit_dict)
