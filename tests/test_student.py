from school_schedule.student import Student


def test_add_class_student():
    student = Student("Bob", "sophmore", ["math", "science"])
    student.add_class("history")
    assert student.classes == ["math", "science", "history"]


def test_add_class_empty():
    student = Student("Jamie", "senior", [])
    student.add_class("home ec")
    assert student.classes == ["home ec"]


def test_get_num_classes():
    student = Student("Bob", "sophmore", ["math", "science"])
    result = student.get_num_classes()
    assert result == 3


def test_get_num_clssses_empty():
    student = Student("Jamie", "senior", [])
    result = student.get_num_classes()
    assert result == 0


def test_get_summary():
    student = Student("Sela", "freshman", ["art", "physics"])
    result = (f"{student.name} is a {student.grade} "
              f"enrolled in {student.get_num_classes()} classes: "
              f"{student.display_classes()}")

    assert result == "Sela is a freshman enrolled in 2 classes: art, physics"
