def found_person_before(people):
    for i in range(len(people)):
        if people[i] == "Don":
            return "Don"
        if people[i] == "John":
            return "John"
        if people[i] == "Kent":
            return "Kent"
    return ""


def found_person_after(people):
    candidates = ["Don", "John", "Kent"]
    for i in range(len(people)):
        if people[i] in candidates:
            return people[i]
    return ""


if __name__ == "__main__":
    people = ["Adam", "Bob", "Charly", "Don", "Frank"]
    print("found_person_after", found_person_after(people))
