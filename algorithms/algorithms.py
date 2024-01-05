

def bubble_sort(array: list, name: str = 'bubble_sort') -> None:
    num_inputs = len(array)

    for i in range(num_inputs):
        # Create a flag that will allow the function to
        # terminate early if there is nothing left to sort
        already_sorted = True

        for j in range(num_inputs - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the 'already_sorted' flag to 'False' so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break


compiled_algorithms = {
    'bubble_sort': bubble_sort
}
