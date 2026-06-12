# ProjectPulse

**ProjectPulse** is a project performance monitoring and business intelligence platform developed with Python and Streamlit. The application provides interactive dashboards, KPI tracking, project status analysis, user authentication, role-based access control, and project management insights through dynamic visualizations.

---

## Features

* User authentication and secure login
* Role-based access control (Admin and Standard User)
* User account management
* Interactive project dashboards
* KPI monitoring and executive indicators
* Project status funnel analysis
* Sector and status filtering
* Budget vs Negotiated Value comparison
* SQLite database integration
* Data processing with Pandas
* Interactive visualizations with Plotly

---

## Tech Stack

* Python
* Streamlit
* Pandas
* Plotly
* SQLAlchemy
* SQLite
* Streamlit Authenticator

---

## Application Screenshots

### Home Page

User welcome screen with navigation shortcuts and application branding.

![Home Page](Images/homepage.png)

---

### Interactive Dashboard

Project value analysis by sector and status with interactive filters.

![Project Dashboard](Images/grafico_setores.png)

---

### Budget vs Negotiated Value Analysis

Comparison between budgeted and negotiated values with yearly filtering.

![Budget Analysis](Images/grafico_barras.png)

---

### KPI Monitoring

Executive KPI overview including project funnel analysis and key business metrics.

![KPIs](Images/kpis.png)

---

### User Management

Admin page for creating new user accounts and managing permissions.

![Create Account](Images/criar_conta.png)

---

### Access Control (Admin)

Administrative menu with access to user management features.

![Admin Menu](Images/menu_admin.png)

---

### Access Control (Standard User)

Restricted menu for standard users.

![Standard User Menu](Images/menu_comum.png)

---

## Project Structure

```text
ProjectPulse/
│
├── main.py
│
├── assets/
│   └── images/
│
├── data/
│   ├── Base.xlsx
│   └── app.db
│
├── pages/
│   ├── homepage.py
│   ├── dashboard.py
│   └── indicadores.py
│
├── src/
│   ├── database/
│   │   └── models.py
│   │
│   ├── services/
│   │   └── data_loader.py
│   │
│   └── auth/
│       └── criar_conta.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Kiiomaru/ProjectPulse.git
cd ProjectPulse
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

```bash
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run main.py
```

---

## Key Skills Demonstrated

* Data Analysis
* Business Intelligence
* Dashboard Development
* Data Visualization
* User Authentication
* Role-Based Access Control (RBAC)
* Database Integration
* Object-Oriented Programming
* Python Application Development

---

## Author

**Matheus Giuliano**

Python Developer | Automation & Data Analytics

* GitHub: https://github.com/Kiiomaru
* LinkedIn: https://linkedin.com/in/magiuliano

---

If you found this project interesting, feel free to connect with me on LinkedIn or explore my other projects focused on Python automation, data analysis, dashboards, and business intelligence.

