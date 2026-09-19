def greet(name: str = "World") -> str:
    return f"Hello, {name}! Welcome to your Python sample project."


def main() -> None:
    print(greet("Hello Developer"))
    print("This project is running successfully.")


if __name__ == "__main__":
    main()
