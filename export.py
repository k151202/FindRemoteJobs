import csv

def save_to_file(jobs):
    file = open("result.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Link"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return