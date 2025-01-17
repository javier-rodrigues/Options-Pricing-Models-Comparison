# Project Setup Instructions

## Prerequisites
Ensure you have the following installed:
- **Python** (for Django backend) - Version 3.8+
- **Node.js** (for React frontend) - Version 16+
- **npm** or **yarn** (Node package managers)

---

## Project Structure
```
project/
├── backend/ (Django)
└── frontend/ (React)
```

---

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Backend Setup (Django)
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Start the Django development server:
   ```bash
   python backend\manage.py runserver
   ```

---

## Frontend Setup (React)
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies using npm:
   ```bash
   npm install
   ```
   **Note:** If you use Yarn instead of npm, run:
   ```bash
   yarn
   ```
3. Start the React development server:
   ```bash
   npm start
   ```


---

## Environment Variables
1. Both backend and frontend use `.env` files for sensitive configurations.
2. Copy the example environment file for each:
   - Backend:
     ```bash
     cp backend/.env.example backend/.env
     ```
   - Frontend:
     ```bash
     cp frontend/.env.example frontend/.env
     ```
3. Update the `.env` files with the required values.

---

## Running the Full Project
source venv/bin/activate  # Activate virtual environment

1. Start the backend (Django) server:
   ```bash
   cd backend
   python manage.py runserver
   ```
2. Start the frontend (React) server in a separate terminal:
   ```bash
   cd frontend
   npm start
   ```
3. Open the application in your browser (usually at `http://localhost:3000`).

---

## Additional Notes
- Ensure ports `3000` (frontend) and `8000` (backend) are available.
- For production deployment, refer to the documentation for tools like Docker or Heroku.
