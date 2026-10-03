# AI Job Application Management System using MCP

## Project Description

This project is an AI-based Job Application Management System built using Python, SQLite, and the Model Context Protocol (MCP).

The system stores information about companies, job applications, and interviews in a SQLite database. MCP tools provide controlled read-only access to this information so that an AI assistant can retrieve and understand the user's job application data.

## Features

- Store company and job application information
- Store interview details
- View all companies
- View all job applications
- View all interviews
- View application details with company names
- Search applications by status
- Search applications by company name
- Read-only database access for safety
- MCP-based tools for AI interaction

## Technologies Used

- Python
- SQLite
- Model Context Protocol (MCP)
- MCP Inspector
- SQL
- Git and GitHub

## Project Structure

```text
Ai-Job_Application MCP/
│
├── server.py
├── database.py
├── schema.sql
├── seed.py
├── README.md
├── BUILD-LOG.md
│
└── data/
    └── placement.db
    ## MCP Tools

### 1. get_companies()

Returns all companies stored in the database.

### 2. get_applications()

Returns all job applications stored in the database.

### 3. get_interviews()

Returns all interview details stored in the database.

### 4. get_application_details()

Returns application details along with company name and job role.

### 5. search_applications_by_status(status)

Searches applications using their status, such as Pending, Interview, or Rejected.

### 6. search_applications_by_company(company_name)

Searches applications using the company name.
## Database Tables

### Companies

Stores company and job information.

- Company ID
- Company Name
- Job Role
- Location
- Status

### Applications

Stores job application information.

- Application ID
- Company ID
- Applied Date
- Application Status
- Notes

### Interviews

Stores interview information.

- Interview ID
- Application ID
- Interview Date
- Interview Round
- Result

## How to Run

## How to Run

### 1. Install dependencies

```bash
python -m pip install mcp
python -m pip install "mcp[cli]"

python seed.py

mcp dev server.py

## Safety

The database is connected in read-only mode through the MCP server.

This prevents MCP tools from modifying or deleting database records.

The system allows the AI assistant to read and retrieve job application information without directly changing the stored data.
## Project Workflow

```text
User Job Application Data
          ↓
     SQLite Database
          ↓
      database.py
          ↓
       server.py
          ↓
      MCP Tools
          ↓
    MCP Inspector
          ↓
     AI Assistant
     ## Future Scope

- Connect the MCP server with an AI assistant
- Add AI-based job application summaries
- Add interview reminders
- Add job application analytics
- Add resume and job description matching
- Add intelligent job search assistance
- Add a web-based dashboard

## Author

Jyoti Salunke

MCA Student