def is_power_of_four(n: int) -> bool:
	if n == 1:
		return True
	elif n < 1:
		return False
	return is_power_of_four(n/4)

if __name__ == "__main__":
	pass