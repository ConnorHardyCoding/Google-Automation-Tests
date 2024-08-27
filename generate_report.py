#!/usr/bin/env python3
import csv

def read_employees(csv_file_location):
        with open(csv_file_location) as file:
                reader = csv.DictReader(file)
                employee_list = [dict(data) for data in reader]
        return employee_list

employee_list  = read_employees("/home/student/data/employees.csv")

def process_data(employee_list):
        department_list = [employee_department[" Department"] for employee_department in e$
        department_data = {department_name: department_list.count(department_name) for dep$
        return department_data

dictionary = process_data(employee_list)

def write_report(dictionary, report_file):
        with open(report_file, "w+") as file:
                for item in sorted(dictionary):
                        file.write(str(item) + ":" + str(dictionary[item]) + "\n")
                file.close()

write_report(dictionary, "/home/student/data/report.txt")