let map = (transform_function) => {
	return (array) => {
		return array.reduce((accum, item) => {
			return accum.concat(transform_function(item));
		})
	}
}
