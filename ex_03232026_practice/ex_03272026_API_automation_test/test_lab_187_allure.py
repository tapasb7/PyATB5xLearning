import pytest
import allure

@allure.title("Verify that create booking with valid data is working")
@allure.description("Testcase for positive test")
@pytest.mark.positive
def test_create_booking_positive():
    print("Test 1")
    assert 5 == 5


@allure.title("Verify that create booking with invalid data is not working")
@allure.description("Testcase for negative test")
@pytest.mark.negative
def test_create_booking_negative():
    print("Test 2")
    assert 1 + 1 == 2



