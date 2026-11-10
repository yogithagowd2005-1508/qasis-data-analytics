"""
OASIS INFOBYTE — SIP (Summer Internship Program)
Intern: C K Yogitha | Intern ID: OIB/O2/IP3782
Track: Data Analytics
GitHub: https://github.com/yogithagowd2005-1508/qasis-data-analytics
LinkedIn: https://www.linkedin.com/in/c-k-yogitha-187129295
Master Automation Runner: Executes all completed tasks end-to-end
"""

import os
import subprocess
import sys
import time

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_task(task_name, script_path):
    print("\n" + "=" * 80)
    print(f" [*] RUNNING: {task_name}")
    print("=" * 80)
    start_time = time.time()
    result = subprocess.run([sys.executable, script_path], capture_output=False)
    elapsed = time.time() - start_time
    if result.returncode == 0:
        print(f" [SUCCESS] {task_name} finished in {elapsed:.2f}s")
    else:
        print(f" [ERROR] {task_name} exited with return code {result.returncode}")
    return result.returncode == 0

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    tasks = [
        ("Level 1 Task 1: EDA on Retail Sales Data", os.path.join(base_dir, "DataAnalytics-L1-EDARetailSales", "eda_retail_sales.py")),
        ("Level 1 Task 2: Customer Segmentation Analysis", os.path.join(base_dir, "DataAnalytics-L1-CustomerSegmentation", "customer_segmentation.py")),
        ("Level 1 Task 3: Data Cleaning & Quality Remediation", os.path.join(base_dir, "DataAnalytics-L1-CleaningData", "data_cleaning.py")),
        ("Level 2 Task 1: House Price Prediction (Linear Regression)", os.path.join(base_dir, "DataAnalytics-L2-HousePricePrediction", "house_price_prediction.py"))
    ]

    print("\n" + "#" * 80)
    print(" OASIS INFOBYTE SIP - DATA ANALYTICS TRACK MASTER TEST RUNNER")
    print("#" * 80)

    success_count = 0
    for name, script in tasks:
        if run_task(name, script):
            success_count += 1

    print("\n" + "#" * 80)
    print(f" FINAL SUMMARY: {success_count}/{len(tasks)} Tasks Executed Successfully!")
    print("#" * 80 + "\n")

if __name__ == "__main__":
    main()
