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


def process_file():
    df = pd.read_excel("data/input.xlsx")

    invalid_amounts = df[df["amount"] <= 0]

    if not invalid_amounts.empty:
        print("\nERROR: Invalid amounts detected:")
        print(invalid_amounts)
        return

    duplicate_requests = df[df.duplicated(subset=["request_id"], keep=False)]

    if not duplicate_requests.empty:
        print("\nERROR: Duplicate request IDs detected:")
        print(duplicate_requests)
        return

    print("\nProcessing input file...")
    print(f"Total records: {len(df)}")

    print("\nData received:")
    print(df)

    pending_review = df[
        (df["status"] == "Pending") &
        (df["amount"] >= 40000)
    ]
    pending_review = pending_review.copy()
    pending_review["review_reason"] = "Pending request with amount >= 40000"

    print("\nRequests requiring review:")
    print(pending_review)
    print("\n--- Processing Summary ---")
    print(f"Total requests: {len(df)}")
    print(f"Requests requiring review: {len(pending_review)}")
    print(f"Requests not requiring review: {len(df) - len(pending_review)}")
    
    pending_review.to_excel("data/review_required.xlsx", index=False)

    print("\nReport generated: data/review_required.xlsx") 

if __name__ == "__main__":
    create_sample_file()
    process_file()