def calculate_statistics(*args):
    if len(args) == 0:
        return {"count": 0, "sum": 0, "average": 0, "min": None, "max": None}
    return {
        "count": len(args),
        "sum": sum(args),
        "average": sum(args) / len(args),
        "min": min(args),
        "max": max(args)
    }

print(calculate_statistics())
print(calculate_statistics(5))
print(calculate_statistics(1, 2, 3, 4, 5))