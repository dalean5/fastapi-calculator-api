from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.get("/add")
async def add(x: int = 0, y: int = 0):
    sum = x + y
    res = {
        "x": x,
        "y": y,
        "result": sum,
    }
    return res


@app.get("/subtract")
async def subtract(x: int = 0, y: int = 0):
    difference = x - y
    res = {
        "x": x,
        "y": y,
        "result": difference,
    }
    return res


@app.get("/multiply")
async def multiply(x: int = 0, y: int = 0):
    product = x * y
    res = {
        "x": x,
        "y": y,
        "result": product,
    }
    return res


@app.get("/divide")
async def divide(x: int = 0, y: int = 0):
    try:
        quotient = x / y
        res = {
            "x": x,
            "y": y,
            "result": quotient,
        }
        return res
    except ZeroDivisionError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"msg": "cannot divide by zero"},
        )
