import uvicorn

if __name__ == "__main__":
    uvicorn.run("server_utility.app:main_app", port=8081, host="0.0.0.0", reload=True)
