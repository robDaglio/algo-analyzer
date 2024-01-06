import json
import logging

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
    with AlgoAnalyzer(algorithms=compiled_algorithms) as algo_analyzer:
        algo_analyzer.run_analysis('bubble_sort')











