
month_conversion = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sept": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december"
}

print(month_conversion["jan"])
print(month_conversion.get("sept"))
print(month_conversion.get("june", "Not a valid month"))

