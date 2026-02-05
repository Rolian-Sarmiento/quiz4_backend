LINK OF THE FRONTEND: https://github.com/Nibe-Git-Hub/quiz4_frontend

Quiz 4 Backend API

A robust RESTful API built with Node.js and Express to manage quizzes, user authentication, and scoring. This backend serves as the core engine for the Quiz 4 application.
🚀 Getting Started
Prerequisites

    Node.js (v14.x or higher)

    npm or yarn

    MongoDB (Local or Atlas)

Installation

    Clone the repository:
    Bash

    git clone https://github.com/Rolian-Sarmiento/quiz4_backend.git
    cd quiz4_backend

    Install dependencies:
    Bash

    npm install

    Environment Variables: Create a .env file in the root directory and add the following:
    Code snippet

    PORT=5000
    MONGO_URI=your_mongodb_connection_string
    JWT_SECRET=your_super_secret_key

    Run the application:
    Bash

    # Development mode
    npm run dev

    # Production mode
    npm start

🛣 API Endpoints
1. Authentication
Method	Endpoint	Description	Auth Required
POST	/api/auth/register	Register a new user	No
POST	/api/auth/login	Login and receive JWT	No
2. Quizzes
Method	Endpoint	Description	Auth Required
GET	/api/quizzes	Get all available quizzes	Yes
GET	/api/quizzes/:id	Get details of a specific quiz	Yes
POST	/api/quizzes	Create a new quiz (Admin)	Yes (Admin)
DELETE	/api/quizzes/:id	Delete a quiz	Yes (Admin)
3. Submissions & Scoring
Method	Endpoint	Description	Auth Required
POST	/api/scores/submit	Submit quiz answers	Yes
GET	/api/scores/user/:id	Get quiz history for a user	Yes
🧪 Testing with Postman

Follow these steps to test the endpoints effectively:
Step 1: Base URL

Set your base URL in Postman as a variable or directly: http://localhost:5000
Step 2: Register & Login

    Select POST and enter {{BASE_URL}}/api/auth/register.

    Go to the Body tab, select raw and JSON.

    Enter:
    JSON

    {
      "username": "testuser",
      "email": "test@example.com",
      "password": "password123"
    }

    Once registered, use the same credentials for the /login endpoint.

Step 3: Handling Authorization (JWT)

Most endpoints require a Bearer Token:

    Copy the token received from the Login response.

    In Postman, go to the Authorization tab of your request.

    Select Type: Bearer Token.

    Paste your token into the Token field.

Step 4: Creating a Quiz (Example)

    Method: POST

    URL: {{BASE_URL}}/api/quizzes

    Body (JSON):
    JSON

    {
      "title": "General Knowledge",
      "questions": [
        {
          "questionText": "What is 2+2?",
          "options": ["3", "4", "5"],
          "correctAnswer": "4"
        }
      ]
    }

🛠 Tech Stack

    Backend: Node.js, Express.js

    Database: MongoDB with Mongoose

    Authentication: JSON Web Tokens (JWT) & Bcrypt.js

    Validation: Express-Validator

📄 License

This project is licensed under the MIT License.
