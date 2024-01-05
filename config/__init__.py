import configargparse


parser = configargparse.get_argument_parser(
    description='Configuration for Algo-Analyzer.',
    formatter_class=configargparse.ArgumentDefaultsRawHelpFormatter,
    default_config_files=['config/defaults.ini']
)

parser.add_argument('-l', '--log-level', type=str, default='INFO',
                    help='The logging level for the application.')

parser.add_argument('-p', '--log-file-path', type=str, default='logs/algo-analyzer.log',
                    help='The logging directory for the application.')
