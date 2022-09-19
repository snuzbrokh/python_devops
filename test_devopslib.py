from devops_lib.randomfruit import fruit

def test_fruit():
    fruit_choice = fruit()
    assert fruit_choice in  ['apple','banana','kiwi']