

customer={
    "name":"Uvindu Karalliyadda",
    "age":30,
    "City":"Kurunegala"
}

print(customer["name"])
print(customer.get("University","SLIIT"))

phone=input("Phone: ")
digits_mapping={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output=""
for ch in phone:
    output+=digits_mapping.get(ch,"!")+" "
print(output)