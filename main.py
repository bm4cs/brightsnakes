import csv


def main():
    domain_counts: dict[str, int] = {}

    with open("D:\\ZEIT8028-DigitalForensics\\MajorForensicsReport\\network\\dns-traffic.csv", "r", newline="") as data:
        reader = csv.DictReader(data)
        for row in reader:
            domain_name = row["Name"]
            if domain_name.rfind("docz.google.com") != -1:
                domain_name = "docz.google.com"
            elif domain_name.rfind("mp.microsoft.com") != -1:
                domain_name = "mp.microsoft.com"
            count = domain_counts.get(domain_name, 0)
            domain_counts[domain_name] = count + 1

    for k, v in sorted(domain_counts.items(), key=lambda i: i[1], reverse=True):
        print(f"{k} {v}")


if __name__ == "__main__":
    main()
