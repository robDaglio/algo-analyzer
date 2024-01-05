import functools
import time
import random
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()
results = []


class AlgoTimer:
    def __init__(
        self,
        iterations: int = 3,
        tests: int = 10,
        num_inputs: int = 1000000,
        input_lower_bound: int = 1,
        input_upper_bound: int = 999
    ):

        self.iterations, self.tests, self.num_inputs = iterations, tests, num_inputs
        self.inputs = []

        self.algos = {
            'generate_random_nums': self.generate_random_numbers
        }

        self.generate_random_numbers(input_lower_bound, input_upper_bound)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    # Operational methods
    @staticmethod
    def timer(method):
        """
        This decorator calculates elapsed time for a given algorithm.
        """
        @functools.wraps(method)
        def timer_wrapper(*args, **kwargs):
            start = time.perf_counter()
            r_value = method(*args, **kwargs)
            results.append(f'Function: {__name__} | Time lapsed: {time.perf_counter() - start}')

            return r_value
        return timer_wrapper

    @timer
    def generate_random_numbers(self, lower_bound: int, upper_bound: int):
        self.inputs = [random.randint(lower_bound, upper_bound) for _ in range(self.num_inputs)]

    def run_algo(self, algo_name: str):
        for _ in range(self.iterations):
            self.algos[algo_name](self.inputs)


if __name__ == '__main__':
    with AlgoTimer(3, tests=10, num_inputs=1000000) as s:
        s.run_algo('generate_random_nums')


