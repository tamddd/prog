let sum = (nums) => {
	return nums.reduce(
		(accum, num) => {
			return accum + num;
		}
	);
}


console.log(sum([1, 2, 3, 4, 5]));
