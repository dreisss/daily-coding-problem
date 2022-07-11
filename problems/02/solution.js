/**
 Map the list and for each element multiply the others and append in the new list.

 # Examples:
 ```
 coding_problem_02([1, 2, 3, 4, 5]); // output [120, 60, 40, 30, 24]
 coding_problem_02([3, 2, 1]); // output [2, 3, 6]
 ```
 */
function coding_problem_02(numbers) {
  let result = [];
  for (let i in numbers) {
    let product = 1;
    for (let j in numbers) if (i != j) product *= numbers[j];
    result.push(product);
  }
  return result;
}
