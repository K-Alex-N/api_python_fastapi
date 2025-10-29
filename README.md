### Multi-Container Python Application for Personal Finance Management

![Image description](https://raw.githubusercontent.com/K-Alex-N/assets/main/docker/main.png)

### 📄 Description  
* **API Service**  
  * RESTful API built with **FastAPI** and **MongoDB**  

* **Tests**  
  * **Isolation** of tests achieved by packaging each test type into its own container  
  * **UI Tests** powered by **Playwright**  
     * Architecture: **Page Object + Page Elements**  
     * A couple of tests are designed to **fail intentionally** to demonstrate automatic screenshot attachment in **Allure reports**  
  * **API Tests** implemented using:  
    * **Pytest**, **Requests**  
    * Data validation via **Pydantic**  
    * Dynamic test data generation with **Faker**  
    * Pre-population of the database before test execution  
  * **Performance Tests** of the API server  
    * Implemented with **Locust**  
    * Running **3 workers in parallel**  
  * **Allure Reports** for clear visualization of test results:  
    * Attach JSON response schemas (in API tests) and screenshots (in UI tests)  
    * Grouping by **epic**, **feature**, **story**  
    * Detailed **allure.steps** for faster defect analysis  

* **Docker**  
  * **Single-command project startup** — launches all **16 containers** (`docker compose up`)
  * **Clean containers** — only necessary files are copied; redundant data is excluded via **.dockerignore**  

* **Monitoring and Logging:**  
  * Logs in **Kibana**  
  * Metrics in **Grafana** (container includes a preconfigured dashboard)  

* **Welcome Page** built with **Flask** — a convenient entry point to all services  

---

### 🚀 Quick Start

**Requirements:** Docker installed  

Clone the repository:
```bash
git clone https://github.com/K-Alex-N/api_python_fastapi.git
cd api_python_fastapi
```
Start:
```bash
docker compose up
```


