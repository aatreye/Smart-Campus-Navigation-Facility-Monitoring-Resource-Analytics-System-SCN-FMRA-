from scripts.week1_basics import welcome
from scripts.week2_io import get_location
from scripts.week3_conditions import validate_location
from scripts.week6_strings import format_path
from scripts.week7_data_structures import (
    create_graph,
    display_graph,
    add_edge,
    add_location,
    remove_location
)
from scripts.week8_advanced_ds import shortest_path
from scripts.week9_oop import Facility
from scripts.week10_files import load_graph, save_graph
from scripts.week11_exceptions import safe_input
from scripts.week12_analytics import generate_report, plot_graph

import csv


# 🔹 1. NAVIGATE
def navigate():
    graph = load_graph()

    if not graph:
        graph = create_graph()
        save_graph(graph)

    start, end = get_location()

    if validate_location(start, graph) and validate_location(end, graph):
        path, distance = shortest_path(graph, start, end)

        print("\nShortest Path:")
        print("Route:", format_path(path))
        print("Distance:", distance)


# 🔹 2. CHECK FACILITY
def check_facility():
    print("\n--- Facility Status ---")

    try:
        with open("data/facilities.csv", "r") as f:
            reader = csv.DictReader(f)

            for row in reader:
                facility = Facility(row["name"], row["status"])
                facility.display()

    except FileNotFoundError:
        print("Facilities file not found!")


# 🔹 3. ANALYZE
def analyze():
    print("\nGenerating Report...")
    generate_report()
    print("Report saved in output/report.txt")


# 🔹 4. GRAPH (SHOW + MODIFY + SAVE + VISUALIZE)
def graph_menu():
    graph = load_graph()

    if not graph:
        graph = create_graph()

    while True:
        print("\n--- Graph Menu ---")
        print("1. Show Graph")
        print("2. Add Location")
        print("3. Add Path")
        print("4. Remove Location")
        print("5. Save & Back")

        choice = safe_input()

        if choice == 1:
            display_graph(graph)


        elif choice == 2:
            loc = input("Enter location: ")
            add_location(graph, loc)

        elif choice == 3:
            src = input("From: ")
            dest = input("To: ")
            dist = safe_input()
            add_edge(graph, src, dest, dist)

        elif choice == 4:
            loc = input("Enter location to remove: ")
            remove_location(graph, loc)

        elif choice == 5:
            save_graph(graph)
            print("Graph saved!")
            break

        else:
            print("Invalid choice!")


# 🔹 MAIN MENU
def main():
    welcome()

    while True:
        print("\n1. Navigate")
        print("2. Check Facility")
        print("3. Analyze")
        print("4. Graph")
        print("5. Exit")

        choice = safe_input()

        if choice == 1:
            navigate()

        elif choice == 2:
            check_facility()

        elif choice == 3:
            analyze()

        elif choice == 4:
            graph_menu()

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()