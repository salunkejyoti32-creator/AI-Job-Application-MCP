# AI Job Application Management System using MCP

## Project Description

This project is an AI-based Job Application Management System built using Python, SQLite, Model Context Protocol (MCP), and a local AI model.

The system stores information about companies, job applications, and interviews in a SQLite database.

The AI assistant allows users to ask questions in normal English. The AI identifies the user's intent and selects the appropriate MCP tool to retrieve the required information from the SQLite database.

The database is accessed through controlled read-only MCP tools for safety.

## Features

* Store company and job application information
* Store interview details
* View all companies
* View all job applications
* View all interviews
* View complete application details
* Search applications by status
* Search applications by company name
* Ask questions using normal English
* AI-based intent classification
* Continuous question-answer interaction
* Read-only database access
* MCP-based tools for AI interaction
* Local AI using Ollama and Qwen

## Technologies Used

* Python
* SQLite
* Model Context Protocol (MCP)
* Ollama
* Qwen 2.5 0.5B
* MCP Inspector
* SQL
* Git and GitHub
* Visual Studio Code

## Project Structure

```text
Ai-Job_Application MCP/
│
├── server.py
├── database.py
├── schema.sql
├── seed.py
├── ai_client.py
├── mcp_client.py
├── README.md
├── BUILD-LOG.md
├── .gitignore
│
└── data/
    └── placement.db
```

## MCP Tools

### 1. get_companies()

Returns all companies stored in the database.

### 2. get_applications()

Returns all job applications stored in the database.

### 3. get_interviews()

Returns all interview details stored in the database.

### 4. get_application_details()

Returns complete application information including company name, job role, applied date, status, and notes.

### 5. search_applications_by_status(status)

Searches applications using their status.

Supported statuses:

* Pending
* Interview
* Rejected

### 6. search_applications_by_company(company_name)

Searches applications using the company name.

## Database Tables

### Companies

Stores company and job information.

* Company ID
* Company Name
* Job Role
* Location
* Status

### Applications

Stores job application information.

* Application ID
* Company ID
* Applied Date
* Application Status
* Notes

### Interviews

Stores interview information.

* Interview ID
* Application ID
* Interview Date
* Interview Round
* Result

## AI Integration

The project uses Ollama to run a local AI model.

Model used:

`qwen2.5:0.5b`

The AI works as an intent classifier.

For example:

```text
User: Show me all companies

AI selects: get_companies
```

Another example:

```text
User: Show me pending applications

AI selects: search_applications_by_status
```

Another example:

```text
User: Show me TCS application

AI selects: search_applications_by_company
```

## Project Workflow

```text
User asks a question in normal English
                ↓
        Local AI (Qwen)
                ↓
        Intent Classification
                ↓
          Select MCP Tool
                ↓
           MCP Server
                ↓
        SQLite Database
                ↓
        Retrieve Information
                ↓
          Display Result
                ↓
         Ask Next Question
```

## Continuous AI Assistant

The application supports continuous interaction.

The user runs:

```bash
python mcp_client.py
```

The program remains open and allows the user to ask multiple questions one by one.

Example:

```text
Ask your AI: Show me all companies

Ask your AI: Show me pending applications

Ask your AI: Show me all interviews

Ask your AI: Show me TCS application
```

The assistant continues running until the user enters:

```text
exit
```

or

```text
quit
```

## How to Run

### 1. Install MCP

```bash
python -m pip install mcp
```

### 2. Install MCP CLI

```bash
python -m pip install "mcp[cli]"
```

### 3. Create the database

```bash
python seed.py
```

### 4. Test the MCP server with Inspector

```bash
mcp dev server.py
```

### 5. Run the AI assistant

```bash
python mcp_client.py
```

Then ask questions in normal English.

## Safety

The database connection is configured in read-only mode.

The MCP tools only retrieve information from the database.

The available MCP tools cannot modify or delete database records.

The SQLite database file is also excluded from GitHub using `.gitignore`.

## GitHub

The project source code is maintained using Git and GitHub.

The database file is not committed to GitHub.

The following project files are maintained in the repository:

* server.py
* database.py
* schema.sql
* seed.py
* ai_client.py
* mcp_client.py
* README.md
* BUILD-LOG.md
* .gitignore

## Future Scope

* Add AI-based job application summaries
* Add interview reminders
* Add job application analytics
* Add resume and job description matching
* Add intelligent job search assistance
* Add a web-based dashboard
* Add more advanced natural-language queries
* Connect with external job portals and APIs

## Author

Jyoti Salunke

MCA Student
