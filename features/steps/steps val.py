from behave import *
from features.odd_number_detailed import input_numbers

@given('Function runss')
def step_impl(context):
    print ('STEP: Given Function runs')

@when('I input string "{num1}" and numeric "{num2}" to function')
def step_impl(context,num1,num2):
    print (f'STEP: When I input {num1} and {num2} to function')
    context.result = input_numbers(num1,num2)

@then('I get result cautious "{warning}"')
def step_impl(context,warning):
    print (f'STEP: Then I get result {warning}')
    context.text =warning
    assert context.result == context.text ,f'{context.result} is not {context.text}'