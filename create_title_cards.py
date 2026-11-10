"""
OASIS INFOBYTE — SIP (Summer Internship Program)
Title Card Generator for Demo Video Submissions (Step 4 of PDF Workflow)
Rule: First 2 seconds must show Full Name, Track, Task Title, and verified credentials.
"""

import os
import tempfile
os.environ["MPLCONFIGDIR"] = os.path.join(tempfile.gettempdir(), "matplotlib")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

def generate_title_card(output_path, intern_name, intern_id, track_name, task_title, task_code, github_url, linkedin_url, date_str):
    # 1920x1080 equivalent at 120 DPI (16 x 9 inches)
    fig, ax = plt.subplots(figsize=(16, 9), facecolor='#0b0f19')
    ax.set_facecolor('#0b0f19')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Outer border gradient effect
    outer_box = FancyBboxPatch((0.025, 0.03), 0.95, 0.94, boxstyle="round,pad=0.015",
                               fc='#111827', ec='#38bdf8', lw=2.5)
    ax.add_patch(outer_box)

    # Top Accent Banner
    banner = FancyBboxPatch((0.025, 0.89), 0.95, 0.08, boxstyle="round,pad=0.01",
                            fc='#1e293b', ec='#0ea5e9', lw=1.5)
    ax.add_patch(banner)

    # Header text
    ax.text(0.5, 0.935, "OASIS INFOBYTE  •  SUMMER INTERNSHIP PROGRAM (OIBSIP)",
            color='#38bdf8', fontsize=18, fontweight='bold', ha='center', va='center', fontfamily='sans-serif')

    # Task Badge
    badge_box = FancyBboxPatch((0.36, 0.79), 0.28, 0.065, boxstyle="round,pad=0.008",
                               fc='#0284c7', ec='#38bdf8', lw=1.5)
    ax.add_patch(badge_box)
    ax.text(0.5, 0.822, task_code.upper(),
            color='#ffffff', fontsize=16, fontweight='bold', ha='center', va='center')

    # Task Title
    ax.text(0.5, 0.71, task_title,
            color='#ffffff', fontsize=30, fontweight='bold', ha='center', va='center', wrap=True)

    # Decorative divider
    ax.plot([0.15, 0.85], [0.63, 0.63], color='#334155', linewidth=1.5)

    # Main Credentials Card Container
    card_box = FancyBboxPatch((0.08, 0.12), 0.84, 0.46, boxstyle="round,pad=0.015",
                              fc='#1e293b', ec='#475569', lw=1.5)
    ax.add_patch(card_box)

    # Details Grid inside Credentials Box
    # Column 1: Intern Name & ID
    ax.text(0.12, 0.51, "INTERN NAME:", color='#94a3b8', fontsize=13, fontweight='bold', va='center')
    ax.text(0.35, 0.51, intern_name, color='#38bdf8', fontsize=22, fontweight='bold', va='center')

    ax.text(0.12, 0.42, "CANDIDATE ID:", color='#94a3b8', fontsize=13, fontweight='bold', va='center')
    ax.text(0.35, 0.42, f"{intern_id}  (Offer Date: {date_str})", color='#f1f5f9', fontsize=16, fontweight='bold', va='center')

    ax.text(0.12, 0.33, "ASSIGNED TRACK:", color='#94a3b8', fontsize=13, fontweight='bold', va='center')
    ax.text(0.35, 0.33, track_name, color='#a855f7', fontsize=18, fontweight='bold', va='center')

    ax.plot([0.11, 0.89], [0.26, 0.26], color='#334155', linewidth=1)

    # Links
    ax.text(0.12, 0.20, "GITHUB REPO:", color='#94a3b8', fontsize=12, fontweight='bold', va='center')
    ax.text(0.35, 0.20, github_url, color='#38bdf8', fontsize=14, fontweight='bold', va='center')

    ax.text(0.12, 0.15, "LINKEDIN:", color='#94a3b8', fontsize=12, fontweight='bold', va='center')
    ax.text(0.35, 0.15, linkedin_url, color='#60a5fa', fontsize=14, fontweight='bold', va='center')

    # Footer Notice
    ax.text(0.5, 0.065, "Mandatory 2-Second Title Card  |  Oasis Infobyte Internship Submission Evaluation",
            color='#64748b', fontsize=12, ha='center', va='center', style='italic')

    plt.tight_layout()
    plt.savefig(output_path, dpi=200, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"Generated enhanced title card: {output_path}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    intern_name = "C K Yogitha"
    intern_id = "OIB/O2/IP3782"
    date_str = "05 October 2026"
    track_name = "Data Analytics"
    github_url = "https://github.com/yogithagowd2005-1508/qasis-data-analytics"
    linkedin_url = "https://www.linkedin.com/in/c-k-yogitha-187129295"

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
        generate_title_card(path, intern_name, intern_id, track_name, title, code, github_url, linkedin_url, date_str)

if __name__ == "__main__":
    main()
