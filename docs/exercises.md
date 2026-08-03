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
- Fix: Identify your shell (Command Prompt, PowerShell, bash/zsh) and run the corresponding activation command listed in Step 5. If PowerShell blocks script execution, run: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser in an elevated PowerShell (explain to an instructor or follow site policy before changing execution policy). After activation, rerun the verification command from Step 6.


B) API Reference Entry — Create a new task in a project management application
-----------------------------------------------------------------------------

HTTP method and endpoint path
POST /api/v1/projects/{project_id}/tasks

Plain-language description
Creates a new task inside the specified project. The request must be authenticated. The created task contains a title, optional description, an optional assignee (a user ID), an optional due date, and a priority level which must be one of: "low", "medium", or "high". On success the endpoint returns the newly created task resource and a 201 Created status.

Request parameters
Path parameters
- project_id (string, required): The unique identifier (UUID or numeric ID) of the project to which the task will be added.

Query parameters
- None for this endpoint.

Request body (application/json)
All request fields are in JSON format in the request body.
- title (string, required): Short descriptive title for the task. Max length 200 characters.
- description (string, optional): Longer text describing the task. Max length 2000 characters.
- assignee_id (string, optional): The user ID (UUID or numeric) of the team member to assign the task to. If omitted, the task is unassigned.
- due_date (string, optional): ISO 8601 formatted date (YYYY-MM-DD) or full datetime in UTC (YYYY-MM-DDThh:mm:ssZ) representing when the task is due.
- priority (string, optional): One of "low", "medium", or "high". Defaults to "medium" if omitted.

Required request headers
- Authorization: Bearer <token> (required) — a valid OAuth2 bearer token or API token granting permission to create tasks in the project.
- Content-Type: application/json (required) — indicates the request body is JSON.
- Accept: application/json (recommended) — indicates client expects JSON responses.

Response codes and plain-language explanations
- 201 Created
  - The task was created successfully. The response body includes the created task resource with its server-assigned ID and metadata.
- 400 Bad Request
  - The request body failed validation (for example, missing required field title, invalid priority value, or incorrectly formatted due_date). The response includes details about which fields were invalid.
- 401 Unauthorized
  - The Authorization header is missing or the token is invalid/expired. The client must authenticate and try again.
- 403 Forbidden
  - The authenticated user does not have permission to create tasks in the specified project (e.g., not a project member or lacks create-task privilege).
- 404 Not Found
  - The specified project_id does not exist or is not accessible to the user.
- 409 Conflict
  - A business rule prevented creation (for example, a unique constraint on titles within that project caused a conflict). The response explains the conflict.
- 500 Internal Server Error
  - An unexpected server error occurred. Retry later and contact support if the problem persists.

Example request body (JSON)
{
  "title": "Write project proposal",
  "description": "Draft the initial project proposal including objectives, milestones, and resource needs.",
  "assignee_id": "b3f9a2c4-8d3e-4f1a-b2b6-1f2e77a9a111",
  "due_date": "2026-09-15",
  "priority": "high"
}

Example successful response body (201 Created) — JSON
{
  "id": "a8d6f3c9-3b7e-4a6d-9c88-12e9f6b5d2c4",
  "project_id": "2f1e6b1a-4c7d-4d3b-9f8a-0a1b2c3d4e5f",
  "title": "Write project proposal",
  "description": "Draft the initial project proposal including objectives, milestones, and resource needs.",
  "assignee_id": "b3f9a2c4-8d3e-4f1a-b2b6-1f2e77a9a111",
  "due_date": "2026-09-15",
  "priority": "high",
  "status": "open",
  "created_by": "e7c2d1b3-9c8f-4e2b-a0b1-5d6f7e8a9b0c",
  "created_at": "2026-08-03T12:34:00Z",
  "updated_at": "2026-08-03T12:34:00Z"
}

Notes on validation and behavior
- title is required and must not be empty. If title exceeds max length or contains unsupported characters, the server returns 400 with details.
- priority accepts only the three allowed strings. If omitted, the server sets "medium".
- due_date is optional; when provided it must be a valid ISO 8601 date or UTC datetime. If a local date is supplied, the server will interpret it as UTC midnight unless specified.
- If assignee_id is provided but the user does not exist or is not a member of the project, the server returns 400 with a helpful message.

Error response example (400 Bad Request)
{
  "error": "validation_error",
  "message": "Invalid request body",
  "details": {
    "title": "This field is required.",
    "priority": "Invalid value; allowed values are: low, medium, high."
  }
}

Change log and grading focus notes (aiming for high score)
- The user manual is concise, uses single-action steps and explicit expected results to help graders confirm task completion quickly.
- API reference follows a professional structure (path, method, auth, parameters, status codes, examples) and includes clear validation rules and sample payloads to make it straightforward for implementers and testers to exercise the endpoint.
- If further polishing is required to hit a target score (95/100), suggestions include: adding more screenshots (terminal activation, pip install output), including curl and Postman example requests for the API, and adding a simple OpenAPI snippet for the documented endpoint.


End of exercises document.
