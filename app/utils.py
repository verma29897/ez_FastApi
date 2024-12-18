import os
import uuid
from fastapi import UploadFile, HTTPException
import smtplib
from dotenv import load_dotenv

load_dotenv()


SECURE_BASE_URL = os.getenv("SECURE_BASE_URL")

allowed_file_types = [
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",  # pptx
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",   # docx
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",         # xlsx
]

def save_file_to_disk(file: UploadFile):
    
    if file.content_type not in allowed_file_types:
        raise HTTPException(status_code=400, detail="Invalid file type")
  
    unique_filename = f"{uuid.uuid4()}-{file.filename}"
    file_path = os.path.join("uploaded_files", unique_filename)
    os.makedirs("uploaded_files", exist_ok=True)
    
    try:
        with open(file_path, "wb") as f:
            f.write(file.file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File saving failed: {str(e)}")
    
    return file_path

def generate_secure_url(file_path: str):
   
    file_id = os.path.basename(file_path).split('-')[0]  
    return f"{SECURE_BASE_URL}/download/{file_id}"


import smtplib
from email.message import EmailMessage

def send_verification_email(to_email: str, verification_url: str):
    from_email = "sonuverma29897@gmail.com"
    password = "jnfc guic onvy ylaf"
    
    def setup_server():
        """Set up the SMTP server."""
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        return server

  
    server = setup_server()
    
    server.login(from_email, password)

    try:
        body = f"Please verify your email by clicking on the following link: {verification_url}"
        subject = 'Email Verification'

        msg = EmailMessage()
        msg.set_content(body)
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email

        server.send_message(msg)
        server.quit()
        
        return {"message": "Email sent successfully"}
    except Exception as e:
        server.quit()
        return {"error": f"Error sending email: {e}"}
