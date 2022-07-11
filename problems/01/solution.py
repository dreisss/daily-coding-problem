def coding_problem_01(numbers: "list[int]", k: int) -> bool:
  """
  Sum each possibility and return True when any result equals k, return False otherwise.

  # Examples:
  ```
  coding_problem_01([10, 15, 3, 7], 17) # return True (10 + 7 = 17)
  coding_problem_01([10, 15, 3, 7], 23) # return False
  ```
  """
  for i in range(numbers.__len__()):
    for j in range(i + 1, numbers.__len__()):
      if numbers[i] + numbers[j] == k:
        return True
  return False

if __name__ == "__main__":
  print(coding_problem_01([10, 15, 3, 7], 23));
