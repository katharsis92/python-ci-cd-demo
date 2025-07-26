```markdown
# 🛠️ Python CI/CD Demo

A simple Python project demonstrating how to set up Continuous Integration (CI) using GitHub Actions.  
Includes basic arithmetic operations and unit tests using `pytest`.

## 📚 Features

- Modular project structure using `app/` and `tests/`
- Unit testing with `pytest`
- GitHub Actions workflow for automated test execution
- Follows best practices with docstrings and clean code

## 📁 Project Structure

```
python-ci-cd-demo/
├── app/
│   └── calculator.py
├── tests/
│   └── test_calculator.py
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── requirements.txt
├── README.md
```

## ⚙️ Technologies Used

- Python 3.10+
- Pytest
- GitHub Actions
- WSL / Linux-based environment (optional)

## 🚀 Getting Started

1. **Clone the repo**

```bash
git clone https://github.com/diksha-rawat/python-ci-cd-demo.git
cd python-ci-cd-demo
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run tests**

```bash
pytest
```

## ✅ CI with GitHub Actions

Every push or pull request to the `main` branch automatically triggers tests via GitHub Actions.

Example workflow: [`.github/workflows/python-ci.yml`](.github/workflows/python-ci.yml)

Using GitHub Actions for CI/CD ensures that:

- 🔁 All code changes are tested automatically
- ❌ Bugs are caught early
- 📦 Code remains stable before merging to `main`
- 🔄 You avoid the need to manually run tests or builds
- 🧪 Your codebase becomes more professional and production-ready

## 🙋‍♀️ About Me

**Diksha Rawat**  
Senior Lead Engineer @ Qualcomm  
🌱 DevOps & CI/CD Enthusiast  
🔗 [GitHub](https://github.com/diksha-rawat)

---

📌 _This project is part of my journey to demonstrate clean, maintainable, and automated Python workflows._
```