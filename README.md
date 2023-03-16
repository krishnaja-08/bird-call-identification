## Bird Call Identification Project

This project allows you to identify bird species based on their calls using a machine learning model trained in Python. The backend is built with Flask and the frontend is built with React (Vite).

### Prerequisites

* **Software:**
    * Git ([https://git-scm.com/](https://git-scm.com/))
    * Python (3.x) ([https://www.python.org/downloads/](https://www.python.org/downloads/))
    * pip (usually comes bundled with Python)
    * Node.js ([https://nodejs.org/en](https://nodejs.org/en))
    * npm (comes bundled with Node.js)
* **Libraries:**
    * Flask ([https://flask.palletsprojects.com/](https://flask.palletsprojects.com/))
    * React (Vite) ([https://vitejs.dev/guide/](https://vitejs.dev/guide/))

### Setup

1. **Clone the repository:**

```bash
git clone https://your-github-repository.com/bird-call-identification.git
```

2. **Navigate to the project directory:**

```bash
cd bird-call-identification
```

3. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

4. **Install frontend dependencies:**

```bash
cd frontend
npm install
```

### Running the project

1. **Start the backend server:**

   Open a terminal in the project directory (`bird-call-identification`) and run:

   ```bash
   python backend/app.py
   ```

   This will typically start the Flask server on port 5000 by default. You can check the specific port in the `app.py` file or any console output during startup.

2. **Run the frontend development server:**

   Open another terminal window (or a new tab in the same terminal) and navigate to the frontend directory:

   ```bash
   cd frontend
   ```

   Then, run:

   ```bash
   npm run dev
   ```

   This will start the React development server, accessible at `http://localhost:5173`.

### Using the application

1. Open your web browser and navigate to `http://localhost:5173`
2. Click on the "Choose File" button and select a bird call recording in a supported audio format (e.g., WAV, MP3).
3. Click on the "Identify Bird" button.
4. The application will process the recording and display the predicted bird species.

**Note:**

* The accuracy of the bird call identification will depend on the quality of the recording and the training data used for the machine learning model.
* This project is for educational purposes and may not be perfect in all situations.


