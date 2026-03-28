class OddNumberGenerator:
    """Class for generating odd numbers.

    Args:
        None

    Returns:
        list: A list of odd numbers from 1 to 10.
    """

    def get_odd_numbers(self, upper_limit: int = 10) -> list:
        """Function to generate and return odd numbers from 1 to upper_limit.

        Args:
            upper_limit (int): Upper limit for generating odd numbers. Defaults to 10.

        Returns:
            list: A list of odd numbers from 1 to upper_limit.

        Raises:
            ValueError: If upper_limit is less than 1.
            TypeError: If upper_limit is not an integer.
        """
        if not isinstance(upper_limit, int):
            raise TypeError("Upper limit must be an integer.")
        if upper_limit < 1:
            raise ValueError("Upper limit must be 1 or greater.")

        # Generate odd numbers from 1 to upper limit
        odd_numbers = [i for i in range(1, upper_limit + 1) if i % 2 != 0]

        return odd_numbers


if __name__ == "__main__":
    odd_generator = OddNumberGenerator()
    try:
        odd_numbers = odd_generator.get_odd_numbers()
        print("Odd numbers from 1 to 10:")
        print(odd_numbers)
    except Exception as e:
        print(f"Error: {e}")