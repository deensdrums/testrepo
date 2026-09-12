# Correct negative-number addition and add regression tests

Update calculator.add to return correct signed integer sum, and augment test suite with regression tests for negative and zero inputs; preserve existing function signature and positive test.

## Interfaces
- def add(a: int, b: int) -> int

## Compatibility
Backward compatible at signature level; behavior change affects correctness of output for negative/zero inputs, but no breaking API change.

## Test strategy
- Run python -m unittest discover -v to confirm all tests pass, including new regression tests for negative/zero inputs and existing positive test.
- Run ruff check . to verify lint compliance.
- Verify CI workflow (.github/workflows/test.yml) executes same tests without failure.

## Risks
- Potential undefined behavior or misalignment if test expectations or implementation logic are mis-specified.
- Risk of incomplete regression coverage if new test cases do not fully match acceptance criteria.
- Risk of lint failures if code style changes are not applied.
