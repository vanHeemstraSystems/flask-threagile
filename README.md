flask-threagile
# Flask Treagile

## Introduction

Here’s a simple example of a Python Flask application using SQLAlchemy, along with the integration of the threagile security vulnerability detection tool.

### Flask Application Example

**Directory Structure:**
```
.
├── flask_app
|   ├── .venv
|   |   └── .keepgit
|   ├── app.py
|   ├── models.py
|   ├── requirements.txt
|   ├── templates
|   |   ├── add_user.html
|   |   ├── delete_user.html
|   |   ├── home.html
|   |   ├── login.html
|   |   └── users.html
|   └── tests
|       └── .keepgit
├── reports
|   └── .keepgit
├── .gitignore
├── README.md
├── threagile.sh
└── threagile_config.yaml
```

**1. `requirements.txt`**
```plaintext
bcrypt
cryptography
Flask
Flask-SQLAlchemy
Werkzeug
```

### How to run the Threagile Docker Container

**Requirements**:

- Docker

Execute Threagile on a model yaml file (via docker) from the root directory of this repository: 

```
$ ./threagile.sh -verbose -model /app/work/threagile.yaml -output /app/work/reports
```

### How to run the Flask Application

**Note**: You can run the Flask Application from within the Threagile Docker Container.

**Requirements**:
- Python3 (If run inside Threagile Docker Container, the Docker Container needs to facilitate Python3).

Run this application as follows:

1) Enter ```flask_app``` directory: ```$ cd flask_app```
2) Run ```pip install -r requirements.txt```
3) If non-existent, create a virtual environment inside the ```flask_app``` directory: ```python3 -m venv .venv```
4) Start the virtual environment and enter: ```. .venv/bin/activate```
5) Set the Flask App to app directory: ```(.venv) $ export FLASK_APP=app```
6) Set the Flask Environment to development: ```(.venv) $ export FLASK_ENV=development```
7) Run the flask app: ```(.venv) $ flask run```
8) Open the web interface as prompted
9) Use ```CTRL+c``` to exit the web server.
10) Alternatively run the flask command line interface: ```(.venv) $ flask shell```
11) Execute any flask commands: >>>
12) Use ```exit()``` to exit from the command line interface.

### Integrating Threagile

To use threagile for vulnerability detection, follow these steps:

1. **Install threagile**: 
   Follow the installation instructions from the [threagile GitHub repository](https://github.com/threagile/threagile).

2. **Run Security Analysis**:
   Once installed, you can run the analysis on your Flask application directory to identify vulnerabilities.

3. **Command Example**:
   ```bash
   threagile analyze ./flask_app
   ```

This setup allows you to build a basic Flask application with SQLAlchemy and integrate security checks using threagile.

The command `threagile analyze ./flask_app` runs the Threagile security analysis tool on the specified directory (`./flask_app`). This command scans the application code for potential security vulnerabilities, such as:

- **Code Injection**: Identifying places where user input could lead to injection attacks.
- **Authentication Issues**: Checking for weak authentication mechanisms.
- **Data Exposure**: Detecting sensitive data handling practices.
- **Dependency Vulnerabilities**: Analyzing third-party libraries for known security issues.

The tool generates a report highlighting any identified vulnerabilities, along with recommendations for remediation.

Threagile typically requires a configuration file, often in YAML format, to specify the analysis settings and parameters. This file allows you to customize the scanning process, including which files to analyze, specific rules to apply, and other configurations. 

Make sure to include a properly formatted YAML file in your repository for effective analysis.

Here’s a sample YAML configuration file for Threagile that you can use for the Flask application:

**`threagile_config.yaml`**

```yaml
# Threagile Configuration File

project:
  name: Flask User Management App
  version: 1.0

scan:
  directories:
    - ./flask_app
  file_types:
    - python
  exclude:
    - tests/
    - venv/
  
rules:
  - name: SQL Injection Prevention
    description: Ensure user inputs are properly sanitized.
    enabled: true

  - name: Password Hashing
    description: Check that passwords are hashed before storage.
    enabled: true

  - name: Sensitive Data Exposure
    description: Identify any plaintext sensitive information.
    enabled: true

report:
  format: markdown
  output: reports/security_report.md
```

### Key Sections
- **project**: Basic information about the project.
- **scan**: Specifies directories to scan and file types to include or exclude.
- **rules**: Lists specific security checks to perform.
- **report**: Configures the format and output location for the analysis report.

Adjust this configuration as needed to suit your specific application and security requirements.

To generate the Threagile report every time the Flask application runs, you can modify the `app.py` file to include a function that executes the Threagile analysis. 

### Explanation
- **`run_threagile` Function**: This function constructs the command to run Threagile and executes it using `subprocess.run()`.
- **`@app.before_first_request` Decorator**: This decorator ensures that the Threagile analysis runs before the first request to the application, generating the report each time the server starts.

### Note
Ensure that Threagile is installed and accessible in your environment. This implementation will generate the report every time you start the Flask application. Adjust the command as necessary based on your specific setup.
