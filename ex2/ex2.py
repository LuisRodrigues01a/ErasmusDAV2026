def create_person(first_name, last_name, age=30, city="Warsaw"):
    return {"first_name": first_name, "last_name": last_name, "age": age, "city": city}

print(create_person("Luis", "Rodrigues"))
print(create_person("Ana", "Silva", 25))
print(create_person("João", "Costa", 40, "Porto"))
print(create_person("Maria", "Santos", city="Lisboa"))