# BUILD LOG — AI Job Application Management System using MCP

## Project Overview

This project is an AI-powered Job Application Management System built using Python, SQLite, MCP (Model Context Protocol), and a local AI model.

The system allows a user to ask questions about job applications in normal English. The AI identifies the user's intention and selects the appropriate MCP tool. The MCP server then retrieves the required information from the SQLite database.

---

## Technologies Used

- Python
- SQLite
- MCP (Model Context Protocol)
- Ollama
- Qwen 2.5 0.5B
- JSON
- Git
- GitHub
- Visual Studio Code

---

## Database

The project uses SQLite as the database.

Database file:

`data/placement.db`

The database contains three main tables:

### 1. Companies

Stores company and job information.

Fields:

- id
- name
- role
- location
- status

### 2. Applications

Stores job application information.

Fields:

- id
- company_id
- applied_date
- status
- notes

### 3. Interviews

Stores interview information.

Fields:

- id
- application_id
- interview_date
- round
- result

---

## MCP Tools

The MCP server provides six tools.

### 1. get_companies()

Returns all companies stored in the database.

### 2. get_applications()

Returns all job applications.

### 3. get_interviews()

Returns all interview records.

### 4. get_application_details()

Returns complete application information including company, role, date, status, and notes.

### 5. search_applications_by_status(status)

Searches applications using their status.

Supported statuses:

- Pending
- Interview
- Rejected

### 6. search_applications_by_company(company_name)

Searches applications using the company name.

---

## AI Integration

The project uses Ollama to run a local AI model.

Model used:

`qwen2.5:0.5b`

The AI works as an intent classifier.

Example:

User:

"Show me all companies"

AI selects:

`get_companies`

Another example:

User:

"Show me pending applications"

AI selects:

`search_applications_by_status`

Another example:

User:

"Show me TCS application"

AI selects:

`search_applications_by_company`

---

## Project Workflow

```text
User asks question
        ↓
Local AI (Qwen)
        ↓
Intent classification
        ↓
Select MCP tool
        ↓
MCP Server
        ↓
SQLite Database
        ↓
Retrieve information
        ↓
Display result to user
        ↓
Ask for next question