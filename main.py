import json

from config import parser
from clu.clu import CLU
from algorithms.algorithms import compiled_algorithms


cfg = parser.parse_known_args()[0]
log = CLU(
    log_level=cfg.log_level,
    log_to_file=True,
    log_file_path=cfg.log_file_path.split('/')[0],
    log_file_name=cfg.log_file_path.split('/')[1]
).get_logger()

log.debug(f'Configuration: {json.dumps(vars(cfg), indent=4)}')


if __name__ == '__main__':
    from analyzer.analyzer import AlgoAnalyzer

    log.info('This is a test.')

    with AlgoAnalyzer(
        algos=compiled_algorithms,
        num_inputs=10
    ) as a:
        a.run_algo(algo_name='bubble_sort')


    from analyzer.analyzer import results

    log.info('Results: =========================================')

    for k, v in results.items():
        log.info(f'{k}: {v}')





