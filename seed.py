import sqlite3
from pathlib import Path

# Create the data folder if it does not exist
Path("data").mkdir(exist_ok=True)

# Connect to the SQLite database
connection = sqlite3.connect("data/placement.db")

# Read and execute the table structure
with open("schema.sql", "r") as file:
    connection.executescript(file.read())

cursor = connection.cursor()

# Add companies
cursor.executemany(
    """
    INSERT INTO companies (name, role, location, status)
    VALUES (?, ?, ?, ?)
    """,
    [
        ("TCS", "Python Developer", "Pune", "Applied"),
        ("Infosys", "Software Developer", "Pune", "Interview"),
        ("Accenture", "Data Analyst", "Pune", "Rejected"),
        ("Blue Yonder", "Application Support Engineer", "Pune", "Applied"),
    ]
)

# Add job applications
cursor.executemany(
    """
    INSERT INTO applications (company_id, applied_date, status, notes)
    VALUES (?, ?, ?, ?)
    """,
    [
        (1, "2026-09-01", "Pending", "Resume submitted"),
        (2, "2026-09-02", "Interview", "Technical interview scheduled"),
        (3, "2026-09-03", "Rejected", "Application closed"),
        (4, "2026-09-04", "Pending", "Waiting for recruiter response"),
    ]
)

# Add interviews
cursor.executemany(
    """
    INSERT INTO interviews (application_id, interview_date, round, result)
    VALUES (?, ?, ?, ?)
    """,
    [
        (2, "2026-09-10", "Technical Round", "Scheduled"),
    ]
)

connection.commit()
connection.close()

print("Database created and sample data inserted successfully!")