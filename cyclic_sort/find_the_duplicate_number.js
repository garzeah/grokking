const find_duplicate = function (nums) {
  let i = 0;

  while (i < nums.length) {
    const j = nums[i] - 1;

    if (nums[i] !== nums[j]) {
      [nums[i], nums[j]] = [nums[j], nums[i]];
    } else i++;
  }

  // If values are not in the right position,
  // then it must be a duplicate
  for (i = 0; i < nums.length; i++) {
    if (nums[i] !== i + 1) {
      return nums[i];
    }
  }
};
