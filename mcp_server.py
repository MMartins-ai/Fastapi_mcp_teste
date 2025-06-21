from fastmcp import FastMCP


mcp = FastMCP("Meu servidor.")

@mcp.tool
def greet(name: str):
    return f"Hello, {name}!"


@mcp.tool
def multiply(a:float, b:float):
    """Multiplica dois números."""
    return a*b


@mcp.resource("data://config")
def get_config() -> dict:
    """Provides the application configuration."""
    return {"theme": "dark", "version": "1.0"}


if __name__ == "__main__":
    mcp.run(transport="streamable-http", port=9000, path='/mcp', host='0.0.0.0')
