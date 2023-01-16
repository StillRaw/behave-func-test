from behave import *
from odd_number_detailed import odd_numbers
import json

@given('Function runs')
def step_impl(context):
    print ('STEP: Given Function runs')

@when('I input "{num1}" and "{num2}" to function')
def step_impl(context,num1,num2):
    print (f'STEP: When I input {num1} and {num2} to function')
    context.result = odd_numbers(num1,num2)

@then('I get result {a_list}')
def step_impl(context,a_list):
    print (f'STEP: Then I get result {a_list}')
    context.a_list = json.loads(a_list)
    assert context.result == context.a_list ,f'{context.result} is not {context.a_list}'