from datetime import datetime

def generate_log(log_data):

    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
        print(f"log file created: {filename}")

    return filename


if __name__ == "__main__":
    sample = ["User logged in", "User updated profile", "Report exported"]
    print(generate_log(sample))