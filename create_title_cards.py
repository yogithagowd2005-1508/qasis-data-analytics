"""
OASIS INFOBYTE — SIP (Summer Internship Program)
Title Card Generator for Demo Video Submissions (Step 4 of PDF Workflow)
Rule: First 2 seconds must show Full Name, Track, and Task Title as a static frame.
"""

import os
import tempfile
os.environ["MPLCONFIGDIR"] = os.path.join(tempfile.gettempdir(), "matplotlib")
import matplotlib.pyplot as plt

def generate_title_card(output_path, intern_name, track_name, task_title, task_code):
    fig, ax = plt.subplots(figsize=(16, 9), facecolor='#0f172a')
    ax.set_facecolor('#0f172a')
    ax.axis('off')

    # Card border decoration
    rect = plt.Rectangle((0.03, 0.04), 0.94, 0.92, fill=False, edgecolor='#38bdf8', linewidth=2.5, linestyle='-')
    ax.add_patch(rect)

    # Header
    ax.text(0.5, 0.84, "OASIS INFOBYTE - SUMMER INTERNSHIP PROGRAM (OIBSIP)",
            color='#94a3b8', fontsize=20, fontweight='bold', ha='center', va='center', fontfamily='sans-serif')

    # Task Badge
    ax.text(0.5, 0.72, f"[{task_code}]",
            color='#38bdf8', fontsize=24, fontweight='bold', ha='center', va='center')

    # Task Title
    ax.text(0.5, 0.60, task_title,
            color='#ffffff', fontsize=32, fontweight='bold', ha='center', va='center', wrap=True)

    # Separator Line
    ax.plot([0.2, 0.8], [0.48, 0.48], color='#334155', linewidth=2)

    # Intern Details
    ax.text(0.5, 0.38, f"Intern Name: {intern_name}",
            color='#f1f5f9', fontsize=26, fontweight='bold', ha='center', va='center')

    ax.text(0.5, 0.28, f"Assigned Track: {track_name}",
            color='#38bdf8', fontsize=24, ha='center', va='center')

    ax.text(0.5, 0.16, "GitHub Repository: OIBSIP | Video Demo Presentation",
            color='#64748b', fontsize=18, ha='center', va='center')

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"Generated title card: {output_path}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    intern_name = "[Intern Full Name]"
    track_name = "Data Analytics"

    cards = [
        (
            os.path.join(base_dir, "DataAnalytics-L1-EDARetailSales", "plots", "title_card_task1.png"),
            "EDA on Retail Sales Data",
            "Level 1 — Task 1"
        ),
        (
            os.path.join(base_dir, "DataAnalytics-L1-CustomerSegmentation", "plots", "title_card_task2.png"),
            "Customer Segmentation Analysis (RFM & K-Means)",
            "Level 1 — Task 2"
        ),
        (
            os.path.join(base_dir, "DataAnalytics-L1-CleaningData", "outputs", "title_card_task3.png"),
            "Data Cleaning & Quality Remediation",
            "Level 1 — Task 3"
        ),
        (
            os.path.join(base_dir, "DataAnalytics-L2-HousePricePrediction", "plots", "title_card_task4.png"),
            "House Price Prediction with Linear Regression",
            "Level 2 — Task 1"
        )
    ]

    for path, title, code in cards:
        generate_title_card(path, intern_name, track_name, title, code)

if __name__ == "__main__":
    main()
