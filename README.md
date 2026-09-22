# ambient-email-agent

An Ambient Agent that responds to a stream of emails.

---

## Prerequisites

This project requires [**uv**](https://docs.astral.sh/uv/), an extremely fast Python package and project manager. `uv` handles Python version management, dependency resolution, and virtual environments automatically.

### Installing `uv`

If you don't already have `uv` installed, install it using the official standalone installer:

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative methods:**
* **Homebrew (macOS/Linux):** `brew install uv`
* **pipx:** `pipx install uv`

Verify your installation:
```bash
uv --version
```

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/jsturtz/ambient-email-agent.git
cd ambient-email-agent
```

### 2. Install dependencies & setup environment
Run `uv sync` to automatically set up the virtual environment and install all dependencies:
```bash
uv sync
```

> [!NOTE]
> You do not need to install Python manually. `uv` will automatically download and configure the exact Python version specified for this project.

### 3. Configure environment variables
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
Open `.env` and add your Google Gemini API key:
```env
GOOGLE_API_KEY="your-actual-api-key"
```
*(Get an API key from [Google AI Studio](https://aistudio.google.com/app/apikey))*

---

## Usage

### Run the Agent
Run the main script using `uv run`:
```bash
uv run python main.py
```

Alternatively, you can activate the virtual environment and run Python directly:

* **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  python main.py
  ```
* **Windows:**
  ```powershell
  .venv\Scripts\activate
  python main.py
  ```
