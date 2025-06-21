from fastapi import FastAPI, status
from fastapi_mcp import FastApiMCP
from routes.usuario import route
from fastapi.middleware.cors import CORSMiddleware

# criando app
app = FastAPI()
app.include_router(route)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=['saúde'])
async def health():
    return {"status": status.HTTP_200_OK}

# Criando servidor mcp baseado no app
mcp = FastApiMCP(
    app,
    name="My API MCP",
    description="Teste de servidor MCP",
    include_tags=["Users", "saúde"])

# Inicializando o servidor MCP
mcp.mount()
