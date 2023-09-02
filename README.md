# salary_slip_genrator_stremlit
This repository contains a web application for generating and viewing employee salary slips. The application is built using Streamlit and interacts with a MySQL database to fetch employee data and generate PDF salary slips. It allows users to select a specific month and employee code to view and download their salary slip as a PDF document.

Key Features:

User-friendly web interface for selecting employees and months.
Fetches employee data from a MySQL database.
Generates PDF salary slips with relevant employee details.
Provides the option to view and download the generated salary slip.
Usage:

Clone this repository to your local machine.
Set up a MySQL database with employee salary data.
Configure the database connection details in the application.
Run the Streamlit application using streamlit run app.py.
Use the web interface to select an employee and month to view or download their salary slip.
Dependencies:

Streamlit
MySQL Connector
ReportLab (for PDF generation)
