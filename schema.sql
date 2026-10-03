CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    location TEXT,
    status TEXT
);

CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    applied_date TEXT,
    status TEXT,
    notes TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE IF NOT EXISTS interviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    application_id INTEGER,
    interview_date TEXT,
    round TEXT,
    result TEXT,
    FOREIGN KEY (application_id) REFERENCES applications(id)
);