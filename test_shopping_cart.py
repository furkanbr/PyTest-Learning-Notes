import pytest
from unittest.mock import Mock

import item_database
from shopping_cart import ShoppingCart

# pytest.fixture is giving us ability to set up our test environment more easily
# We can write all preparing codes that we use multiple times and run at everytime we use it.
@pytest.fixture
def cart():
    # All preparing stept for cart here...
    return ShoppingCart()

# While defining test cases, function name should start with "test" word.
def test_can_add_item_to_cart(cart):
    cart.add("apple")
    assert cart.size() == 1

def test_when_item_added_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()

# "with pytest.raises" method is used for when python should throw an error with specific condition
# In this example, test case expecting OverFlowError from Python and test passes if it throws error
def test_when_add_more_than_max_item_should_fail(cart):
    for _ in range(5):
        cart.add("apple")
    with pytest.raises(OverflowError):
        cart.add("apple")

# To run just one specific test we can run this command on terminal;
# pytest test_shopping_cart.py::test_can_get_total_price
# to print everything on terminal from test function, just add -s at the end of the command

def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    priceMap = item_database.ItemDatabase()
    # priceMap.get = Mock(return_value=1.5) # Mock method forcing get method to return specific value
    def mock_get_price(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0 # We can use dictionary or anything to return input specific values

    # side_effect is used for pushing to return different values depending on input
    priceMap.get = Mock(side_effect=mock_get_price)
    assert cart.get_total_price(priceMap) == 3
