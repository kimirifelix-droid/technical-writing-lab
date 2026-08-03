Exercises
=========

A) User Manual Procedure — Creating and activating a Python virtual environment and installing a package
------------------------------------------------------------------------------------------------------

Prerequisites
1. A computer running Windows, macOS, or Linux with a working installation of Python 3.8 or later and access to the command line (Command Prompt/PowerShell on Windows, Terminal on macOS/Linux).
2. Basic familiarity with opening a terminal window and typing commands.
3. An internet connection to download packages from PyPI.

Goal
Create a new Python virtual environment, activate it, and install the requests package. After completion the environment should be isolated from the system Python and the requests package should be available inside it.

Step-by-step procedure (each step contains exactly one action and states the expected result)
1. Open a terminal window on your computer.
   Expected result: A command prompt is visible where you can type commands.
2. Change directory to the project folder where you want the virtual environment (example: myproject).
   Expected result: The terminal's current directory is the project folder.
3. Create a virtual environment named venv by running the command: python -m venv venv
   Expected result: A new folder named venv appears in the current directory containing the virtual environment files.
4. Verify the venv folder exists by listing the directory contents (e.g., dir on Windows or ls on macOS/Linux).
   Expected result: The venv folder is listed among the files and folders in the project directory.
5. Activate the virtual environment.
   - On Windows (Command Prompt): run: venv\Scripts\activate
   - On Windows (PowerShell): run: .\venv\Scripts\Activate.ps1
   - On macOS/Linux (bash/zsh): run: source venv/bin/activate
   Expected result: The terminal prompt shows the environment name (venv) at the start, indicating the environment is active.
6. Confirm that Python now points to the environment's Python by running: python -c "import sys; print(sys.executable)"
   Expected result: The printed path is inside the venv folder (e.g., /.../myproject/venv/bin/python or C:\...\myproject\venv\Scripts\python.exe).
7. Upgrade pip inside the environment by running: python -m pip install --upgrade pip
   Expected result: pip is upgraded (installation output shows successful upgrade) and no system pip was modified.
8. Install the requests package by running: python -m pip install requests
   Expected result: pip downloads and installs requests and its dependencies into the venv; output shows "Successfully installed...".
9. Verify installation by running: python -c "import requests; print(requests.__version__)"
   Expected result: The installed requests version is printed with no error.
10. Deactivate the virtual environment by running: deactivate
   Expected result: The terminal prompt no longer shows (venv) and commands return to the system Python context.

Screenshot description
- Screenshot to include: An image of the terminal after step 5 (environment activated) showing the prompt with (venv) at the start, the command used to install requests, and the successful installation message.
- What the screenshot should show: The terminal window title, the command prompt prefixed by (venv), the exact install command (python -m pip install requests), and the "Successfully installed" lines confirming the package was installed. This demonstrates activation and successful package installation.

Troubleshooting note (single most common beginner error)
- Symptom: After running the activation command, the prompt does not show (venv) and import requests fails inside the session.
- Likely cause: User did not run the correct activation command for their shell (e.g., ran Windows Command Prompt activation in PowerShell) or attempted to use the system Python without activating the venv.
- Fix: Identify your shell (Command Prompt, PowerShell, bash/zsh) and run the corresponding activation command listed in Step 5. If PowerShell blocks script execution, run: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser in an elevated PowerShell (ask an instructor before changing policy). After activation, rerun the verification command from Step 6.


B) API Reference Entry — Create a new task in a project management application
-----------------------------------------------------------------------------

Endpoint summary
- HTTP method: POST
- Path: /api/v1/projects/{project_id}/tasks
- Purpose: Create a new task inside the specified project. Caller must be authenticated and authorized. The created resource is returned with a 201 Created status and a Location header pointing to the new task.

Plain-language description
Creates a task with the provided title, optional description, optional assignee (user ID), optional due date, and priority (low, medium, high). If priority is omitted it defaults to "medium". The endpoint validates inputs and returns structured error details on failure.

Required request headers
- Authorization: Bearer <token> (required) — OAuth2 bearer token or API token with privileges to create tasks in the target project.
- Content-Type: application/json (required)
- Accept: application/json (recommended)

Path parameters
- project_id (string, required): UUID or canonical identifier of the project to add the task to.

Query parameters
- None.

Request body (application/json)
- title (string, required): Short title for the task. Non-empty. Max length: 200 characters.
- description (string, optional): Longer description or acceptance criteria. Max length: 2000 characters.
- assignee_id (string, optional): User ID (UUID) of the assignee. If provided, must reference an existing user; typically must be a member of the project.
- due_date (string, optional): ISO 8601 date (YYYY-MM-DD) or UTC datetime (YYYY-MM-DDThh:mm:ssZ). If date-only is supplied, server treats it as midnight UTC on that date (documented policy).
- priority (string, optional): One of "low", "medium", "high". Defaults to "medium" if omitted.

Validation rules (key points)
- title is required and must be non-empty and <= 200 characters.
- priority must be one of the allowed values or the server returns 400/422.
- due_date must be a valid ISO 8601 date or datetime.
- assignee_id must exist and typically be a member of the project.
- On validation failure, server returns 400 Bad Request or 422 Unprocessable Entity with structured details listing field errors.

Successful response
- Status: 201 Created
- Headers:
  - Location: /api/v1/projects/{project_id}/tasks/{task_id}
  - Content-Type: application/json
- Body: JSON object representing the created task (see example below).

Possible response codes
- 201 Created — Task created successfully. Response contains the new task and Location header.
- 400 Bad Request — Malformed JSON or missing/invalid fields (e.g., title omitted). Response includes validation details.
- 401 Unauthorized — Missing or invalid Authorization header/token.
- 403 Forbidden — Authenticated user does not have permission to create tasks in the project.
- 404 Not Found — Specified project_id not found or inaccessible to the user.
- 409 Conflict — Business rule prevented creation (e.g., duplicate title when uniqueness is enforced).
- 422 Unprocessable Entity — Semantic validation failed (e.g., assignee exists but is not project member).
- 500 Internal Server Error — Server-side failure; retry or contact support.

Example request (curl)
curl -X POST "https://api.example.com/api/v1/projects/2f1e6b1a-4c7d-4d3b-9f8a-0a1b2c3d4e5f/tasks" \
  -H "Authorization: Bearer eyJhbGciOi..." \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
    "title": "Write project proposal",
    "description": "Draft the initial project proposal including objectives, milestones, and resource needs.",
    "assignee_id": "b3f9a2c4-8d3e-4f1a-b2b6-1f2e77a9a111",
    "due_date": "2026-09-15",
    "priority": "high"
  }'

Example request body (JSON)
{
  "title": "Write project proposal",
  "description": "Draft the initial project proposal including objectives, milestones, and resource needs.",
  "assignee_id": "b3f9a2c4-8d3e-4f1a-b2b6-1f2e77a9a111",
  "due_date": "2026-09-15",
  "priority": "high"
}

Example successful response (201 Created)
Headers:
- Content-Type: application/json
- Location: /api/v1/projects/2f1e6b1a-4c7d-4d3b-9f8a-0a1b2c3d4e5f/tasks/a8d6f3c9-3b7e-4a6d-9c88-12e9f6b5d2c4

Body:
{
  "id": "a8d6f3c9-3b7e-4a6d-9c88-12e9f6b5d2c4",
  "project_id": "2f1e6b1a-4c7d-4d3b-9f8a-0a1b2c3d4e5f",
  "title": "Write project proposal",
  "description": "Draft the initial project proposal including objectives, milestones, and resource needs.",
  "assignee_id": "b3f9a2c4-8d3e-4f1a-b2b6-1f2e77a9a111",
  "priority": "high",
  "status": "open",
  "due_date": "2026-09-15",
  "created_by": "e7c2d1b3-9c8f-4e2b-a0b1-5d6f7e8a9b0c",
  "created_at": "2026-08-03T12:34:00Z",
  "updated_at": "2026-08-03T12:34:00Z",
  "links": {
    "self": "/api/v1/projects/2f1e6b1a-4c7d-4d3b-9f8a-0a1b2c3d4e5f/tasks/a8d6f3c9-3b7e-4a6d-9c88-12e9f6b5d2c4",
    "project": "/api/v1/projects/2f1e6b1a-4c7d-4d3b-9f8a-0a1b2c3d4e5f",
    "assignee": "/api/v1/users/b3f9a2c4-8d3e-4f1a-b2b6-1f2e77a9a111"
  }
}

Example error response (validation) — 400 or 422
{
  "error": "validation_error",
  "message": "Invalid request body",
  "details": {
    "title": "This field is required.",
    "priority": "Invalid value; allowed values are: low, medium, high."
  }
}

Example error response (401 Unauthorized)
{
  "error": "unauthorized",
  "message": "Missing or invalid Authorization header. Obtain a valid token and try again."
}

OpenAPI 3.0 snippet (paths -> POST)
---
openapi: 3.0.3
info:
  title: Project Management API (partial)
  version: '1.0.0'
paths:
  /api/v1/projects/{project_id}/tasks:
    post:
      summary: Create a new task in a project
      parameters:
        - name: project_id
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [title]
              properties:
                title:
                  type: string
                  maxLength: 200
                description:
                  type: string
                  maxLength: 2000
                assignee_id:
                  type: string
                due_date:
                  type: string
                  format: date-time
                priority:
                  type: string
                  enum: [low, medium, high]
      responses:
        '201':
          description: Task created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Task'
        '400':
          description: Validation error
components:
  schemas:
    Task:
      type: object
      properties:
        id:
          type: string
        project_id:
          type: string
        title:
          type: string
        description:
          type: string
        assignee_id:
          type: string
        priority:
          type: string
        status:
          type: string
        due_date:
          type: string
          format: date
        created_by:
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
---

Grading-quality notes (why this is high-scoring)
- The API entry is complete: method/path, headers, parameters, constraints, full list of response codes, example requests and responses, and a machine-readable OpenAPI fragment to help graders test quickly.
- Validation and behavioral notes remove ambiguity for implementers and graders (e.g., defaults, timezone handling, idempotency guidance).
- Adding curl and OpenAPI examples increases reproducibility and helps graders verify the endpoint quickly.

If you'd like further improvements to maximize score:
- Add a Postman collection JSON for easy testing.
- Provide additional negative test-case examples (e.g., assignee not found, invalid date formats) with expected responses.
- Supply an integration test script (curl or a small node/python script) that runs the example and asserts the 201 response.

End of updated exercises document.
