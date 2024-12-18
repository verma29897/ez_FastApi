# Writing Test Cases

## Unit Test Cases for Signup (`/signup`)

### Test Case: Successfully Create a User
- **Input:** Valid email and password.  
- **Expected Result:** Response should return `201 Created` and a success message.  
- **Validation:** The user is saved in the database, and an email verification link is generated.

### Test Case: Duplicate Email Registration
- **Input:** Existing email in the database.  
- **Expected Result:** Response should return `400 Bad Request` with the message "Email already registered".

### Test Case: Invalid Email Format
- **Input:** Invalid email (e.g., `user@com`).  
- **Expected Result:** Response should return `422 Unprocessable Entity`.

### Test Case: Missing Password
- **Input:** Email provided, but no password.  
- **Expected Result:** Response should return `422 Unprocessable Entity`.

## Unit Test Cases for Email Verification (`/verify/{token}`)

### Test Case: Successful Email Verification
- **Input:** Valid token corresponding to a user.  
- **Expected Result:** Response should return `200 OK` with the message "Email verified successfully".

### Test Case: Invalid Token
- **Input:** A token that does not exist or has expired.  
- **Expected Result:** Response should return `400 Bad Request` or `404 Not Found`.

### Test Case: Expired Token
- **Input:** Token that has exceeded its validity period.  
- **Expected Result:** Response should return `401 Unauthorized` with an appropriate message.

## Unit Test Cases for Login (`/login`)

### Test Case: Successful Login
- **Input:** Valid email and password.  
- **Expected Result:** Response should return `200 OK` with an `access_token`.

### Test Case: Invalid Password
- **Input:** Valid email but incorrect password.  
- **Expected Result:** Response should return `401 Unauthorized` with the message "Invalid credentials".

### Test Case: Unregistered Email
- **Input:** Email not registered in the database.  
- **Expected Result:** Response should return `401 Unauthorized`.

## Unit Test Cases for File Download (`/download-file/{file_id}`)

### Test Case: Successful File Download
- **Input:** Valid `file_id` and token.  
- **Expected Result:** Response should return `200 OK` with a valid `download_link`.

### Test Case: Invalid File ID
- **Input:** File ID that does not exist in the database.  
- **Expected Result:** Response should return `404 Not Found`.

### Test Case: Unauthorized Access
- **Input:** No token provided or invalid token.  
- **Expected Result:** Response should return `401 Unauthorized`.

## Unit Test Cases for Utility Functions

### Test Case: Generate a Secure URL
- **Input:** Valid `file_path`.  
- **Expected Result:** Generated URL should match the format `SECURE_BASE_URL/download/{uuid}`.

### Test Case: Save File to Disk
- **Input:** `UploadFile` instance.  
- **Expected Result:** File should be saved successfully, and its path returned.

---

# Deployment Plan

## Prepare the Application
1. **Dependencies:** Ensure all dependencies are specified in `requirements.txt`.  
2. **Environment Variables:** Use `.env` files for sensitive configurations like database URLs, secret keys, etc.  
3. **Static Files:** Configure FastAPI to serve static files if applicable.  
4. **Secure Routes:** Validate that all endpoints requiring authentication use token-based authentication.
