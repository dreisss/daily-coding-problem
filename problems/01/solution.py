def coding_problem_01(numbers: "list[int]", k: int) -> bool:
  for i in range(numbers.__len__()):
    for j in range(i + 1, numbers.__len__()):
      if numbers[i] + numbers[j] == k:
        print(numbers[i], numbers[j])
        return True
  return False
