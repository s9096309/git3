student = {
    "name": "Peter",
    "grades": [1, 5, 2],
    "lastname": "Wurst"
}

def show_info(student):
    # Access values from the dictionary using keys
    print(f"""
    Name: {student['name']},
    Grades: {student['grades']},
    Last Name: {student['lastname']}
""")

# Call the function
show_info(student)
