import pandas as pd


def create_sample_file():
    data = {
        "request_id": [1001, 1002, 1003, 1004, 1005],
        "customer": [
            "Ana Gomez",
            "Lucas Perez",
            "Maria Lopez",
            "Juan Torres",
            "Sofia Martinez"
        ],
        "amount": [15000, 42000, 8500, 73000, 21000],
        "status": [
            "Pending",
            "Pending",
            "Approved",
            "Pending",
            "Rejected"
        ]
    }

    df = pd.DataFrame(data)

    df.to_excel("data/input.xlsx", index=False)

    print("Input file created successfully.")


if __name__ == "__main__":
    create_sample_file()