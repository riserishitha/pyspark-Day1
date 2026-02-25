# PySpark Day 1 – Environment Setup Guide

This document describes the clean setup process for a PySpark development environment using **Python 3.10** and **Java 11**, including virtual environment creation, dependency installation, and configuration fixes.

---

## 🔧 Prerequisites

Ensure the following are installed on your system:

* **Python**: Version 3.10
* **Java**: Version 11
* **pip** (comes with Python)

Verify versions:

```bash
python --version
java -version
```

---

## 📁 Environment Reset

Deactivate and remove any existing virtual environment:

```bash
deactivate
rm -rf spark-env
```

---

## 🧪 Create Virtual Environment

Create a new isolated Python environment:

```bash
python -m venv spark-env
```

Activate the environment (Windows):

```bash
source spark-env/Scripts/activate
```

---

## 📦 Install PySpark

Install the required PySpark version:

```bash
pip install pyspark==3.5.1
```

---

## ⚙️ One-Time Environment Fix

Set Python paths for PySpark:

```bash
export PYSPARK_PYTHON=python
export PYSPARK_DRIVER_PYTHON=python
```

> ⚠️ Note: On Windows PowerShell, use:

```powershell
setx PYSPARK_PYTHON python
setx PYSPARK_DRIVER_PYTHON python
```

---

## 🧠 System Configuration Fix

Disable **App Installer Aliases** in Windows Settings:

Turn **OFF**:

* `python.exe`
* `python3.exe`

Path:

```
Settings → Apps → App Execution Aliases
```

---

## ✅ Testing Setup

Test Python:

```bash
python
```

(Optional PySpark Test):

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").getOrCreate()
spark.version
```

---

## 📌 Summary

* Python: 3.10
* Java: 11
* Virtual Env: spark-env
* PySpark: 3.5.1
* Aliases Disabled: python.exe, python3.exe
* Env Vars Set: PYSPARK_PYTHON, PYSPARK_DRIVER_PYTHON

---

Environment is now clean, isolated, and ready for Py
