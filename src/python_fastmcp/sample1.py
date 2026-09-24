from fastmcp import FastMCP

mcp = FastMCP("Sample 1")

@mcp.tool(app=True)
def greet(name: str) -> str:
  return f"Hello, {name}!"

@mcp.tool(app=True)
def add(a: int, b: int) -> int:
  return a + b

if __name__ == "__main__":
  mcp.run(transport="http", host="0.0.0.0", port=8000)