# CIH Bank Customer Feedback Analysis

The goal of this project is to create a robust data warehouse solution that enables a thorough analysis of customer feedback for each branch of CIH Bank. In today's highly competitive banking sector, understanding customer sentiment and feedback is crucial for banks to improve their services, enhance customer satisfaction, and make data-driven decisions.

## Project Objectives 🎯

The primary objectives of this project are as follows:

- **Create a Data Warehouse:** Develop a robust system to store and manage customer feedback data from CIH Bank branches.
- **Analyze Customer Feedback:** Perform a comprehensive analysis of customer sentiments, ratings, and reviews to gain valuable insights into their experiences.
- **Improve Banking Services:** Provide CIH Bank with actionable insights to enhance customer satisfaction and continuously improve their services.
- **Utilize Modern Technologies:** Leverage modern technologies and Application Programming Interfaces (APIs), with a focus on the Apify Google Maps Scraper API for data collection.
- **Sentiment Analysis:** Employ a sentiment analysis model to categorize reviews into positive, neutral, or negative sentiments for a deeper understanding.
- **Quantitative Assessment:** Calculate the number of reviews for each branch, helping to identify areas requiring special attention or improvement.
- **Deliver Comprehensive Analysis:** Utilize APIs and custom data aggregation methods to provide CIH Bank with a comprehensive and actionable analysis, equipping them with the insights needed to make informed decisions and enhance customer satisfaction.

## Project Architecture 🏛️

The project's architecture includes the following components:

- **Apify**: Used for data extraction from online sources.
- **Airflow**: Manages the scheduling and execution of data processing tasks.
- **BERT**: A natural language processing (NLP) model for sentiment analysis.
- **PostgreSQL**: The relational database where data is stored.
- **Power BI**: Used for data visualization.

## Project Structure 📂

The project structure is as follows:

- `code`: Directory containing project code:<br>
        - `etl.py`: Python script for the ETL process<br>
        - `extract.py`: Python script for data extraction<br>
        - `load.py`: Python script for data loading<br>
        - `transform.py`: Python script for data transformation<br>
- `CIH_Banks.csv`: Dataset containing customer feedback data<br>
- `Project Report.pdf`: a comprehensive report on the project<br>

## Used Technologies & Tools ⚙️

<img src="https://upload.wikimedia.org/wikipedia/commons/2/28/Apify-logo.svg" height=50/><a href="https://airflow.apache.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/d/de/AirflowLogo.png" alt="Airflow"  height="40"/></a><img src="https://cdn.gptfrance.ai/storage/2023/03/hf-logo-270x270.png" height=50/><a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"> <img src="https://www.postgresql.org/media/img/about/press/elephant.png" alt="postgresql" width="40" height="40"/> </a><a href="https://powerbi.microsoft.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.windowsreport.com/wp-content/uploads/2019/07/Fix-Power-BI-error-blank-values-error.jpg" alt="powerBI" width="40" height="40"/> </a>


