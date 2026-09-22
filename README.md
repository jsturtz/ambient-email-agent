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

### 3. Running commands
You can run any script or command directly inside the managed environment using `uv run`:
```bash
uv run python <script.py>
```

Alternatively, you can activate the virtual environment directly:

* **macOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```
* **Windows:**
  ```powershell
  .venv\Scripts\activate
  ```
