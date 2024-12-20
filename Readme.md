
# All Test Cases and Deployment Plan

## Unit Test Cases

### Signup Endpoint (/signup)
#### Test Case: Successfully Create a User
- **Input:** Valid email and password.
- **Expected Result:** Response returns 201 Created with a success message.
- **Validation:** User is saved in the database, and an email verification link is generated.

#### Test Case: Duplicate Email Registration
- **Input:** Existing email in the database.
- **Expected Result:** Response returns 400 Bad Request with the message "Email already registered".

#### Test Case: Invalid Email Format
- **Input:** Invalid email (e.g., user@com).
- **Expected Result:** Response returns 422 Unprocessable Entity.

#### Test Case: Missing Password
- **Input:** Email provided, but no password.
- **Expected Result:** Response returns 422 Unprocessable Entity.

### Email Verification Endpoint (/verify/{token})
#### Test Case: Successful Email Verification
- **Input:** Valid token corresponding to a user.
- **Expected Result:** Response returns 200 OK with the message "Email verified successfully".

#### Test Case: Invalid Token
- **Input:** A token that does not exist or has expired.
- **Expected Result:** Response returns 400 Bad Request or 404 Not Found.

#### Test Case: Expired Token
- **Input:** Token that has exceeded its validity period.
- **Expected Result:** Response returns 401 Unauthorized with an appropriate message.

### Login Endpoint (/login)
#### Test Case: Successful Login
- **Input:** Valid email and password.
- **Expected Result:** Response returns 200 OK with an access_token.

#### Test Case: Invalid Password
- **Input:** Valid email but incorrect password.
- **Expected Result:** Response returns 401 Unauthorized with the message "Invalid credentials".

#### Test Case: Unregistered Email
- **Input:** Email not registered in the database.
- **Expected Result:** Response returns 401 Unauthorized.

### File Download Endpoint (/download-file/{file_id})
#### Test Case: Successful File Download
- **Input:** Valid file_id and token.
- **Expected Result:** Response returns 200 OK with a valid download_link.

#### Test Case: Invalid File ID
- **Input:** File ID not found in the database.
- **Expected Result:** Response returns 404 Not Found.

#### Test Case: Unauthorized Access
- **Input:** No token provided or invalid token.
- **Expected Result:** Response returns 401 Unauthorized.

### Utility Functions
#### Test Case: Generate a Secure URL
- **Input:** Valid file_path.
- **Expected Result:** Generated URL matches the format SECURE_BASE_URL/download/{uuid}.

#### Test Case: Save File to Disk
- **Input:** UploadFile instance.
- **Expected Result:** File is saved successfully, and its path is returned.

## Deployment Plan

### Prepare the Application
1. **Dependencies:** Verify all dependencies are listed in `requirements.txt`.
2. **Environment Variables:** Use `.env` files for sensitive configurations (e.g., database URLs, secret keys).
3. **Static Files:** Configure FastAPI to serve static files if required.
4. **Secure Routes:** Validate that endpoints requiring authentication use token-based mechanisms.

### Setup and Run the Project
1. Clone the Repository: `git clone <repository_url>`
2. Change Directory: `cd ez_fasti`
3. Create a Virtual Environment: `python -m venv venv`
4. Activate the Virtual Environment:
   - **Windows:** `venv\Scripts\activate`
   - **macOS/Linux:** `source venv/bin/activate`
5. Install Required Dependencies: `pip install -r requirements.txt`
6. Run the Application: `python main.py`
