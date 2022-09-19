from devops_lib.randomfruit import fruit, meal


def test_fruit():
    fruit_choice = fruit()
    assert fruit_choice in ["apple", "banana", "kiwi"]


def test_meal():
    results = meal("MILK")
    assert "MILK" in results
