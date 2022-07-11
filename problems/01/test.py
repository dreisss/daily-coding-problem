from solution import coding_problem_01

test_examples: list[list[list[int] | int | bool]] = [
  [[10, 15, 3, 7], 17, True],
  [[30, 12, 2, 14], 26, True],
  [[30, 12, 2, 14], 15, False],
  [[37, 1, 2, 3], 15, False],
  [[10, 14, 2, 8], 24, True],
  [[10, 14, 2, 8], 10, True],
  [[10, 14, 2, 8], 16, True],
]

def test_solution(test_list: list[list[list[int] | int | bool]]):
  for i, test in enumerate(test_list):
    print(f"Test {i + 1} - ", end="")
    assert coding_problem_01(test[0], test[1]) == test[2], f"Shoud be {test[2]}"
    print("Ok")

if __name__ == "__main__":
  test_solution(test_examples)
