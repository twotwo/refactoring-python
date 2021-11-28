def acquire_data(lines):
    first_line = True
    result = []
    for line in lines:
        if first_line:
            first_line = False
            continue
        if line.strip() == "":
            continue
        record = line.split(",")
        if record[1].strip() == "India":
            result.append({"city": record[0].strip(), "phone": record[2].strip()})

    return result


def acquire_data_stage1(lines):
    next(lines)  # skip first line
    result = []
    loop_items = [line for line in lines if line.strip()]
    for line in loop_items:
        record = line.split(",")
        if record[1].strip() == "India":
            result.append({"city": record[0].strip(), "phone": record[2].strip()})

    return result


def acquire_data_stage2(lines):
    next(lines)  # skip first line
    loop_items = [line.split(",") for line in lines if line.strip()]
    result = [
        {"city": record[0].strip(), "phone": record[2].strip()}
        for record in loop_items
        if record[1].strip() == "India"
    ]

    return result


def acquire_data_stage3(lines):
    next(lines)  # skip first line
    result = [
        {"city": record[0].strip(), "phone": record[2].strip()}
        for record in [line.split(",") for line in lines if line.strip()]
        if record[1].strip() == "India"
    ]

    return result


if __name__ == "__main__":
    with open("office.csv") as f:
        print("=== origin ===\n", acquire_data(f))
    with open("office.csv") as f:
        # print("=== stage1 ===\n", acquire_data_stage1(f))
        print("=== stage3 ===\n", acquire_data_stage3(f))
