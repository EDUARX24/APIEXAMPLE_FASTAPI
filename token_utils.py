import jwt


def createToken(data: dict):
    token : str = jwt.encode(payload=data,key = 'secret',algorithm='HS256')
    return token

def validateToken(token: str)-> dict:
    try:
        data = dict = jwt.decode(token, 'secret', algorithms=['HS256'])
        return data
    except jwt.ExpiredSignatureError:
        return {"message": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"message": "Invalid token"}
    except Exception as e:
        return {"message": "Error occurred", "error": str(e)}