import asyncio
import json
import ollama

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


MODEL = "qwen2.5:0.5b"


def format_result(tool_name, data):

    print("\n" + "=" * 50)

    if tool_name == "get_companies":

        print("COMPANIES")
        print("=" * 50)

        for row in data:
            print(
                f"{row['name']} - "
                f"{row['role']} - "
                f"{row['location']} - "
                f"{row['status']}"
            )

    elif tool_name == "get_applications":

        print("APPLICATIONS")
        print("=" * 50)

        for row in data:
            print(
                f"{row['id']}. "
                f"Company ID: {row['company_id']} | "
                f"Date: {row['applied_date']} | "
                f"Status: {row['status']} | "
                f"Notes: {row['notes']}"
            )

    elif tool_name == "get_interviews":

        print("INTERVIEWS")
        print("=" * 50)

        for row in data:
            print(
                f"Application ID: {row['application_id']} | "
                f"Date: {row['interview_date']} | "
                f"Round: {row['round']} | "
                f"Result: {row['result']}"
            )

    elif tool_name == "get_application_details":

        print("APPLICATION DETAILS")
        print("=" * 50)

        for row in data:
            print(
                f"{row['company']} - "
                f"{row['role']} | "
                f"Date: {row['applied_date']} | "
                f"Status: {row['status']} | "
                f"Notes: {row['notes']}"
            )

    elif tool_name in (
        "search_applications_by_status",
        "search_applications_by_company"
    ):

        print("SEARCH RESULTS")
        print("=" * 50)

        for row in data:
            print(
                f"{row['company']} - "
                f"{row['role']} | "
                f"Date: {row['applied_date']} | "
                f"Status: {row['status']} | "
                f"Notes: {row['notes']}"
            )


async def process_question(session, tool_names, question):

    prompt = f"""
You are an AI intent classifier for a Job Application Management System.

Available MCP tools:
{tool_names}

User question:
{question}

Choose the correct MCP tool.

Rules:

Companies -> get_companies

Applications -> get_applications

Interviews -> get_interviews

Complete application information -> get_application_details

Applications with a specific status -> search_applications_by_status

Applications from a specific company -> search_applications_by_company

For status search use:
Pending, Interview, or Rejected.

Return ONLY valid JSON.

Examples:

{{"name":"get_companies","arguments":{{}}}}

{{"name":"get_interviews","arguments":{{}}}}

{{"name":"search_applications_by_status","arguments":{{"status":"Pending"}}}}

{{"name":"search_applications_by_company","arguments":{{"company_name":"TCS"}}}}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0,
            "num_predict": 60
        }
    )

    content = response["message"]["content"].strip()

    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    try:
        request = json.loads(content)

    except json.JSONDecodeError:

        print("\nAI response could not be understood.")
        print(content)
        return

    tool_name = request.get("name")
    arguments = request.get("arguments", {})

    if tool_name not in tool_names:

        print("\nInvalid MCP tool selected.")
        return

    print(f"\nMCP Tool: {tool_name}")

    tool_result = await session.call_tool(
        tool_name,
        arguments=arguments
    )

    result_text = ""

    for item in tool_result.content:

        if hasattr(item, "text"):
            result_text += item.text

    try:

        data = json.loads(result_text)

    except json.JSONDecodeError:

        print("\nCould not read MCP result.")
        print(result_text)
        return

    format_result(tool_name, data)


async def main():

    print("Starting AI Job Application Assistant...")

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            print("MCP connected!")

            result = await session.list_tools()

            tool_names = [
                tool.name
                for tool in result.tools
            ]

            print("\nType 'exit' to close the assistant.")

            while True:

                question = input("\nAsk your AI: ").strip()

                if question.lower() in ("exit", "quit"):

                    print("\nAI Job Application Assistant closed.")
                    break

                if not question:

                    continue

                await process_question(
                    session,
                    tool_names,
                    question
                )


if __name__ == "__main__":
    asyncio.run(main())