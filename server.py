
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("research-demo")


@mcp.tool()
def add(a: float, b: float) -> dict:
    """Add two numbers and return the result."""
    return {"result": a + b}


@mcp.tool()
def calculate_percentage(part: float, whole: float) -> dict:
    """Calculate what percentage part is of whole."""
    if whole == 0:
        raise ValueError("whole must not be zero")
    return {"percentage": (part / whole) * 100}


@mcp.resource("project://overview")
def project_overview() -> str:
    """Provide a short overview of this demo project."""
    return (
        "This is a demonstration MCP server. "
        "It exposes safe arithmetic tools and a project overview resource."
    )


@mcp.prompt()
def explain_result(question: str) -> str:
    """Create a reusable prompt for explaining a result clearly."""
    return (
        "Explain the following question or result step by step. "
        "State assumptions and check calculations.\n\n"
        f"Input: {question}"
    )


if __name__ == "__main__":
    mcp.run()
