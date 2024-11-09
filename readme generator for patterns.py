patterns_checklist = [
    {
        "name": "Right-Angled Triangle Pattern",
        "completed": False,
        "pattern": [
            "*",
            "* *",
            "* * *",
            "* * * *",
            "* * * * *"
        ]
    },
    {
        "name": "Inverted Right-Angled Triangle",
        "completed": False,
        "pattern": [
            "* * * * *",
            "* * * *",
            "* * *",
            "* *",
            "*"
        ]
    },
    {
        "name": "Pyramid Pattern",
        "completed": False,
        "pattern": [
            "    *",
            "   * *",
            "  * * *",
            " * * * *",
            "* * * * *"
        ]
    },
    {
        "name": "Diamond Pattern",
        "completed": False,
        "pattern": [
            "    *",
            "   * *",
            "  * * *",
            " * * * *",
            "* * * * *",
            " * * * *",
            "  * * *",
            "   * *",
            "    *"
        ]
    },
    {
        "name": "Pascal's Triangle",
        "completed": False,
        "pattern": [
            "    1",
            "   1 1",
            "  1 2 1",
            " 1 3 3 1",
            "1 4 6 4 1"
        ]
    },
    {
        "name": "Number Pyramid",
        "completed": False,
        "pattern": [
            "    1",
            "   2 3 2",
            "  3 4 5 4 3",
            " 4 5 6 7 6 5 4",
            "5 6 7 8 9 8 7 6 5"
        ]
    },
    {
    "name": "Number Diamond",
    "completed": True,
    "pattern": [
        "    1",
        "   1 2 1",
        "  1 2 3 2 1",
        " 1 2 3 4 3 2 1",
        "1 2 3 4 5 4 3 2 1",
        " 1 2 3 4 3 2 1",
        "  1 2 3 2 1",
        "   1 2 1",
        "    1"
    ]
    },
    {
        "name": "Hourglass Pattern",
        "completed": False,
        "pattern": [
            "* * * * *",
            " * * * *",
            "  * * *",
            "   * *",
            "    *",
            "   * *",
            "  * * *",
            " * * * *",
            "* * * * *"
        ]
    },
    {
        "name": "Hollow Diamond",
        "completed": False,
        "pattern": [
            "    *",
            "   * *",
            "  *   *",
            " *     *",
            "*       *",
            " *     *",
            "  *   *",
            "   * *",
            "    *"
        ]
    },
    {
        "name": "Checkerboard Pattern",
        "completed": False,
        "pattern": [
            "* * * * *",
            " * * * * *",
            "* * * * *",
            " * * * * *",
            "* * * * *"
        ]
    },
    {
        "name": "Number Wave",
        "completed": False,
        "pattern": [
            "1 2 3 4 5 4 3 2 1",
            "  1 2 3 4 3 2 1",
            "    1 2 3 2 1",
            "      1 2 1",
            "        1"
        ]
    },
    {
        "name": "Floyd's Triangle",
        "completed": False,
        "pattern": [
            "1",
            "2 3",
            "4 5 6",
            "7 8 9 10",
            "11 12 13 14 15"
        ]
    },
    {
        "name": "Arrowhead Pattern",
        "completed": False,
        "pattern": [
            "*",
            "* *",
            "* * *",
            "* * * *",
            "* * *",
            "* *",
            "*"
        ]
    },
    {
        "name": "Hollow Square",
        "completed": False,
        "pattern": [
            "* * * * *",
            "*       *",
            "*       *",
            "*       *",
            "* * * * *"
        ]
    },
    {
        "name": "Zigzag Number Pattern",
        "completed": False,
        "pattern": [
            "1 2 3 4 5",
            " 10 9 8 7 6",
            "11 12 13 14 15",
            " 20 19 18 17 16"
        ]
    },
    {
        "name": "Binary Triangle",
        "completed": False,
        "pattern": [
            "1",
            "0 1",
            "1 0 1",
            "0 1 0 1",
            "1 0 1 0 1"
        ]
    }
]

def print_checklist(checklist):
    print("## Pattern Making Progress Checklist\n")
    for item in checklist:
        status = " " if not item["completed"] else "x"
        print(f"- [{status}] **{item['name']}**")
        print("  ```")
        for line in item["pattern"]:
            print(f"  {line}")
        print("  ```\n")

print_checklist(patterns_checklist)