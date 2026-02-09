from jose import jwt
from fastapi import HTTPException

AUTH0_DOMAIN = "your-domain.auth0.com"
API_AUDIENCE = "your-api-identifier"
ALGORITHMS = ["RS256"]

# Example public key (normally fetched from Auth0 JWKS)
PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
YOUR_PUBLIC_KEY_HERE
-----END PUBLIC KEY-----"""

def verify_token(token: str):
    try:
        payload = jwt.decode(
            token,
            key=PUBLIC_KEY,
            algorithms=ALGORITHMS,
            audience=API_AUDIENCE,
            issuer=f"https://{AUTH0_DOMAIN}/"
        )
        return payload
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

# Example usage
if __name__ == "__main__":
    fake_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
    try:
        print(verify_token(fake_token))
    except Exception as e:
        print("Token rejected")
