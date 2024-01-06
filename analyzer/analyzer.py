import logging
import random
import time

from main import log


class AlgoAnalyzer:
    def __init__(
        self,
        algorithms: dict = None,
        tests: int = 3,
        iterations: int = 10,
        num_inputs: int = 10,
        input_lower_bound: int = 1,
        input_upper_bound: int = 99
    ):
        self.algorithms = algorithms
        self.tests, self.iterations = tests, iterations

        self.num_inputs = num_inputs
        self.input_lower_bound, self.input_upper_bound = input_lower_bound, input_upper_bound

        self.analysis_results = {}

    def __str__(self):
        return vars(self)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def generate_inputs(self):
        log.info(f'Creating inputs for {self.tests} tests.')
        inputs = []

        for _ in range(self.tests):
            log.info(f'Generating a new array of {self.num_inputs} random numbers between '
                     f'{self.input_lower_bound} and {self.input_upper_bound}.')

            new_array = [random.randint(self.input_lower_bound, self.input_upper_bound)
                         for _ in range(self.num_inputs)]

            inputs.append(new_array)

        return inputs

    def run_analysis(self, algo_name: str = None):
        for i in range(self.iterations):
            log.info(f'Initiating {algo_name} | Iteration {i + 1}')
            iteration_result = []

            inputs = self.generate_inputs()

            for j in range(len(inputs)):
                start = time.perf_counter()
                sorted_array = self.algorithms[algo_name](inputs[j], name=algo_name)
                elapsed = time.perf_counter() - start

                if sorted_array == sorted(inputs[j]):
                    iteration_result.append(elapsed)

            log.info(f'Iteration {i} complete. Lowest time: {min(iteration_result)}')
            self.analysis_results[f'{algo_name}_{i + 1}'] = min(iteration_result)
            self.interpret_results()

    def interpret_results(self):
        for iteration, result in self.analysis_results.items():
            log.info(f'Iteration: {iteration} | Result: {result}')

        log.info(f'Lowest: {min(list(self.analysis_results.values()))}')
