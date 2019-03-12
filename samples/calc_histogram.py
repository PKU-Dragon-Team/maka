import sys
from optparse import IndentedHelpFormatter, OptionGroup, OptionParser
from os.path import dirname, join

import matplotlib.pyplot as plt
from dotenv import load_dotenv

import maka.inquirer as inquirer

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def main():
    """
    The method called when running this script
    """
    usage = """calc_histogram.py --expr "expresion"
A command-line tool to test similarity to Microsoft's Academic Knowledge."""

    fmt = IndentedHelpFormatter(max_help_position=50, width=100)
    parser = OptionParser(usage=usage, formatter=fmt)
    group = OptionGroup(
        parser, 'Query arguments',
        'These options define search query arguments and parameters.')
    group.add_option(
        '-e', '--expresion', metavar='EXPR', default=None, help='Expression')
    group.add_option(
        '-a', '--attributes', metavar='ATTR', default='Id', help='Expression')
    parser.add_option_group(group)
    options, _ = parser.parse_args()

    # Show help if we have not an expression
    if len(sys.argv) == 1:
        parser.print_help()
        return 1
    if options.expresion is None:
        print('Expression is mandatory!')
        return 1

    query = inquirer.AcademicQuerier(inquirer.AcademicQueryType.HISTOGRAM, {
        'expr': options.expresion,
        'attributes': options.attributes
    })
    if query is not None:
        histograms = query.post()
        for histogram in histograms:
            data = histogram['data']
            rng = list(range(1, len(data) + 1))
            labels = [val['value'] for val in data]
            plt.bar(rng, [val['count'] for val in data])
            plt.xticks(rng, labels, rotation='vertical')
            plt.margins(0.2)
            plt.subplots_adjust(bottom=0.15)
            plt.legend()
            plt.xlabel(histogram['attribute'])
            plt.ylabel('count')
            plt.title('Histogram for {}'.format(histogram['attribute']))
            plt.show()


if __name__ == '__main__':
    sys.exit(main())
