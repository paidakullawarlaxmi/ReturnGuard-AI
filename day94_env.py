from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
secret = os.getenv("SECRET_KEY")
project = os.getenv("PROJECT")

print("="*40)
print("ReturnGuard AI Configuration")
print("="*40)

print("Project :", project)
print("Email   :", email)
print("Password:", password)
print("Secret  :", secret)