def process_input(lines):
    reports = [[int(num) for num in line.strip().split()] for line in lines]
    # print(reports)
    safe_reports = []
    unsafe_reports = []
    for report in reports:
        if check_report_safe(report) == True:
            safe_reports.append(report)
        else:
            unsafe_reports.append(report)
    # print(safe_reports)
    # print(unsafe_reports)
    unsafe_reports_with_tolerance = []
    for report in unsafe_reports:
        if check_report_with_tolerance(report) == True:
            unsafe_reports_with_tolerance.append(report)
    return len(safe_reports), len(safe_reports)+len(unsafe_reports_with_tolerance)

def check_report_safe(report):
    previous_direction = 0
    for i in range(1, len(report)):
        if abs(report[i]-report[i-1]) < 1 or abs(report[i]-report[i-1]) > 3:
            return False
        direction = 1 if report[i] > report[i-1] else -1
        if previous_direction != 0 and direction != previous_direction:
            return False
        previous_direction = direction
    return True

def check_report_with_tolerance(report):
    # Try removing each number and check if the resulting report is safe
    for i in range(len(report)):
        # Create a new list without the number at index i
        modified_report = report[:i] + report[i+1:]
        if check_report_safe(modified_report):
            return True
    return False

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    result = process_input(lines)
    print(result)
    return result  # Return value for testing

if __name__ == "__main__":
    main()