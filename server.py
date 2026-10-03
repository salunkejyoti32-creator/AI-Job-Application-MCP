from mcp.server.mcpserver import MCPServer
from database import get_connection

mcp = MCPServer("AI Job Application Manager")


@mcp.tool()
def get_companies():
    """Get all companies stored in the database."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, role, location, status
        FROM companies
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows
@mcp.tool()
def get_applications():
    """Get all job applications stored in the database."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, company_id, applied_date, status, notes
        FROM applications
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows
@mcp.tool()
def get_interviews():
    """Get all interviews stored in the database."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, application_id, interview_date, round, result
        FROM interviews
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows
@mcp.tool()
def get_application_details():
    """Get job applications with company names and job roles."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            applications.id,
            companies.name,
            companies.role,
            applications.applied_date,
            applications.status,
            applications.notes
        FROM applications
        JOIN companies
        ON applications.company_id = companies.id
    """)

    rows = cursor.fetchall()
    connection.close()

    return rows
@mcp.tool()
def search_applications_by_status(status: str):
    """Search job applications by their status."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            applications.id,
            companies.name,
            companies.role,
            applications.applied_date,
            applications.status,
            applications.notes
        FROM applications
        JOIN companies
        ON applications.company_id = companies.id
        WHERE applications.status = ?
    """, (status,))

    rows = cursor.fetchall()
    connection.close()

    return rows
@mcp.tool()
def search_applications_by_company(company_name: str):
    """Search job applications by company name."""
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            applications.id,
            companies.name,
            companies.role,
            applications.applied_date,
            applications.status,
            applications.notes
        FROM applications
        JOIN companies
        ON applications.company_id = companies.id
        WHERE companies.name LIKE ?
    """, (f"%{company_name}%",))

    rows = cursor.fetchall()
    connection.close()

    return rows

if __name__ == "__main__":
    mcp.run()