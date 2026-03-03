# 📊 Email-Driven Financial Data Automation & BI Reporting Pipeline

An end-to-end automated financial data ingestion and reporting system that processes email-based attachments, orchestrates workflow automation, consolidates datasets, and generates dynamic Power BI dashboards.

---

## 🚀 Project Overview

Organizations often receive financial reports via email attachments from multiple stakeholders. Manual downloading, organizing, and dashboard updates are time-consuming and error-prone.

This project automates the complete pipeline:

- Email filtering  
- Workflow orchestration  
- Cloud storage staging  
- Data ingestion  
- Data transformation  
- Dashboard reporting  

The system ensures consistent, structured, and near real-time financial reporting.

---

## 🏗 System Architecture

![Architecture Diagram](architecture/financial-project.png)

The pipeline follows a layered architecture:

### 1️⃣ Email Ingestion Layer
- Outlook monitors incoming emails  
- Filters based on keywords and sender rules  
- Extracts attachments automatically  

### 2️⃣ Workflow Orchestration Layer
- n8n workflow triggers on new emails  
- Categorizes attachments  
- Uploads raw files to Google Drive  

### 3️⃣ Data Storage Layer
- Google Drive acts as staging area  
- Structured folder organization  
- Raw financial datasets stored securely  

---

## 🛠 Tech Stack

- Microsoft Outlook  
- n8n (Workflow Automation)  
- Google Drive  
- Python (pandas, file handling)  
- Power BI (Power Query + DAX)  

---

## 👤 Author

Mohd Amir  
B.Tech Information Technology  
Data Analytics & Automation  

---

## ⭐ Key Highlights

- Automated email-based financial reporting  
- Integrated workflow orchestration (n8n)  
- Implemented Python-based ingestion layer  
- Built Power BI dashboards with business KPIs  
- Designed scalable layered architecture  
