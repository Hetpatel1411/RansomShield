# RansomShield – Real-Time Ransomware Detection System

## Overview

RansomShield is a Python-based cybersecurity project designed to monitor file system activity and identify ransomware-like behavior in real time. The system continuously observes file modifications and generates alerts when suspicious patterns, such as rapid and repeated file changes, are detected.

The project also provides a monitoring dashboard, forensic evidence collection, and incident logging to help users understand and analyze potential ransomware activity.

---

## Features

* Real-time file system monitoring
* Detection of rapid file modifications
* Ransomware activity alerts
* Live security dashboard
* Forensic evidence collection
* Process monitoring using Psutil
* Incident response logging
* System resource monitoring (CPU, RAM, Disk)
* Streamlit-based user interface

---

## Technologies Used

* Python 3.13
* Watchdog
* Psutil
* Streamlit
* Pandas
* Plotly

---

## How It Works

1. The system continuously monitors selected directories.
2. File modification events are tracked in real time.
3. Multiple rapid modifications within a short time window trigger a ransomware alert.
4. Evidence is collected, including:

   * Timestamp
   * Target file
   * Modification count
   * Running processes
5. Alert information is displayed on the dashboard.
6. Response actions are logged for analysis.

---

## Project Architecture

File Monitoring → Detection Engine → Alert Generation → Evidence Collection → Dashboard Visualization

---

## Screenshots

### Real-Time Detection Engine

Shows ransomware-like activity detection based on rapid file modifications.

### Security Dashboard

Displays alerts, system statistics, and monitoring information.

### Ransomware Alert Visualization

Provides a visual representation of security events and system status.

### Forensic Evidence Collection

Records evidence useful for incident investigation and analysis.

---

## Project Limitations

* Uses rule-based detection logic.
* Simulates ransomware behavior for educational purposes.
* Does not perform automatic process termination.
* Does not isolate devices from networks automatically.
* Not intended for production environments.

---

## Future Enhancements

* Machine Learning–based detection
* Real-time network monitoring
* Automated threat response
* Email and mobile notifications
* Multi-directory monitoring
* Cloud-based dashboard integration

---

## Educational Purpose

This project was developed as part of the GTU Skill-Based Training Program (SBTP) 2026 to explore cybersecurity concepts related to ransomware detection, file monitoring, process analysis, and security incident visualization.

---

## Author

Het Patel 

Diploma in Information Technology

R.C. Technical Institute

Ahmedabad, Gujarat, India
