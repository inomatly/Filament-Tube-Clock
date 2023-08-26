import os
import xml.etree.ElementTree as ET
import sys

def find_latest_report(directory='./reports'):
    reports = [f for f in os.listdir(directory) if f.startswith('report_') and f.endswith('xml')]
    return max(reports) if reports else None

def get_failures_from_report(report_file):
    #レポートからailuresの数を取得する。
    directory='./reports/'
    tree= ET.parse(directory+report_file)
    root = tree.getroot()
    testsuite = root.find('testsuite')
    if testsuite is not None:
        return int (testsuite.get('failures', '0'))
    return 0

def main():
    last_report = find_latest_report()
    if not last_report:
        print("No test report found.")
        sys.exit(1)

    failures = get_failures_from_report(last_report)
    if failures > 0:
        print(f"{failures} failures found in the latest report: {last_report}")
        sys.exit(1)
    else:
        print(f"No failures found in latest report: {last_report}")

if __name__=="__main__":
    main()