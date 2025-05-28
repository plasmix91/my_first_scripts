from fastapi import FastAPI 

app = FastAPI(title="NetAuto API") 
 
@app.get("/") # root endpoint, returns a welcome message 
async def root(): 
    return {"message": "Welcome to NetAuto API"} 

@app.get("/health") # health check endpoint, returns a status message 
async def health_check(): 
    return {"status": "healthy"} 
