## Intro to unit tests

*note: if on a Mac or Linux machine, you may need to replace python with python3 , and pip with pip3.*

### binary

Loop over valid inputs, compare to expected outputs.

Run from /binary directory with

```
python test_bin_to_dec.py
```
or
```
python -m unittest
```

### camel_case

A dictionary of inputs with expected outputs.

Also uses patching to patch the built-in input and output functions to test user input, and the correct output being printed.  Notice use of with patch context manager, which takes care of un-patching when done. Otherwise, you might need to replace the original input/print functions.  

Run from /camel_case directory with

```
python test_camel_case.py
```
or
```
python -m unittest
```


### guest_list

More examples of patching input and print, and mocking the display_menu function;  use of call_args_list with mocking.
Two separate test files, one for testing the data being stored, the other for user interface functionality.

Since there's more than one test, it's convenient to run all at the same time. Unittest supports test discovery, the default behavior when run from /guest_list directory with

```
python -m unittest
```

Or can run one file of tests, as in the other examples


### Recycling truck

Remember this one from Java? There's a Java version with [JUnit tests here](https://github.com/minneapolis-edu/lab4_recycling)

Run tests, in the same way as the preceding examples.

```
python test_recycling_truck.py
```
or
```
python -m unittest
```

### triangle

Covered in the lecture, test coverage discussed.
Tests in separate directory to code - organizing test code and actual code is recommended.

Run unit tests with

```
python -m unittest tests/test_triangle.py
```

To run coverage, first install coverage

```
pip install coverage
```

From the triangle directory

```
coverage coverage run --source=.  -m unittest tests/test_triangle.py
coverage report -m
```

### Cellphone

Your turn. Some of the tests are not finished. Some of the code is not finished. Can you complete this project? Finish all the TODOs in the code.
