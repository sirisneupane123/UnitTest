from behave import *
import PostiveTestCase


@Given(' we have a number')
def step_impl(context):
    pass


@When('the sum is correct')
def step_impl(context):
    assert sum(1,1) == 2


@Then('the test is valid')
def step_impl(context):
    pass