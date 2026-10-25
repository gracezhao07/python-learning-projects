applications = [
    {"application_id": "APP001", "student_name": "Alice", "email": "",
     "programme_id": "BUS001", "transcript_uploaded": True},
    {"application_id": "APP002", "student_name": "Ben", "email": "ben@example.com",
     "programme_id": "BUS002", "transcript_uploaded": True},
    {"application_id": "APP003", "student_name": "Chloe", "email": "chloe@example.com",
     "programme_id": "BUS003", "transcript_uploaded": False},
]

required_fields = [
    "student_name",
    "email",
    "programme_id"
]

for application in applications:
    missing_fields = []
    for field in required_fields:
        if not application[field]:
             missing_fields.append(field)
    if not application["transcript_uploaded"]:
             missing_fields.append('academic transcript')
    print(f"Application: {application['application_id']}")

    if not missing_fields:
        print("Status: Ready to submit")

    else:
        print("Status: Incomplete")
        print(f"Missing: {missing_fields}")
    print()







    