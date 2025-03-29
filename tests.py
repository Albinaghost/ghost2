from interpreter import run_code
"""
+ +1
- -1
. print
, input
> next cell
< prev cell
[ 
]
"""
def test_output_on_start():
    result = run_code("Ook! Ook.")

    assert result == chr(0)

def test_increament_and_output():
    result = run_code("Ook. Ook.\nOok! Ook.")

    assert result == chr(1)

def test_decreament_and_output():
    result = run_code("Ook! Ook! Ook! Ook.")

    assert result == chr(255)
def test_go_left_and_output():
    result = run_code("Ook. Ook. Ook? Ook. Ook! Ook.")

    assert result == chr(0)
def test_go_right_and_output():
    result = run_code("Ook! Ook! Ook. Ook? Ook! Ook.")

    assert result == chr(0)
def test_more_output():
    result = run_code("Ook! Ook. Ook! Ook.")
    assert result == chr(0) + chr(0)
def test_input_and_output():
    result = run_code("Ook. Ook! Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook? Ook. Ook! Ook! Ook! Ook! Ook.", chr(10)+chr(5))
    assert result == chr(12) + chr(4)
test_output_on_start()
test_increament_and_output()
test_decreament_and_output()
test_go_right_and_output()
test_more_output()
test_input_and_output()
test_go_left_and_output()
# def test_input_and_output():
#     result = run_code("++.>,-.", chr(10)+chr(5))
#     assert result == chr(2) + chr(9)
