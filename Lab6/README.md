# Elevator Dispatch

A small Python project for practicing code and branch coverage. The module chooses an elevator's direction, door action, and which elevator should answer a call.

## Run the tests

Install the test tools:

```powershell
python -m pip install pytest coverage
```

From the `lab6` directory, measure code coverage:

```powershell
python -m coverage run --source=elevator_dispatch -m pytest CodeCoverageTest_38_elevator_dispatch.py
python -m coverage report -m
```

Measure branch coverage:

```powershell
python -m coverage run --branch --source=elevator_dispatch -m pytest CodeCoverageTest_38_elevator_dispatch.py BranchCoverageTest_38_elevator_dispatch.py
python -m coverage report -m
```

The test suites achieve 95% code coverage and 100% branch coverage.
