import matplotlib.pyplot as plt
import csv


def generate_report():
    with open("output/report.txt", "w") as f:
        f.write("Campus Usage Report Generated\n")


def plot_graph():
    """
    Plot facility usage as bar chart (like your image)
    """
    names = []
    usage = []

    try:
        with open("data/facilities.csv", "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                names.append(row["name"])

                # Assign numeric value (simulate usage)
                if row["status"] == "Open":
                    usage.append(3)
                else:
                    usage.append(1)

        plt.figure()
        plt.bar(names, usage)
        plt.title("Facility Usage")

        plt.savefig("output/facility_usage.png")
        plt.show()

        print("Graph saved as output/facility_usage.png")

    except FileNotFoundError:
        print("Facilities file not found!")