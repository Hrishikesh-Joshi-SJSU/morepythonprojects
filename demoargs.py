# ----------------------------------------------------------------------
# Name:        demoargs
# Purpose:     demonstrate the use of the argparse module
#
# Author:      Rula Khayrallah
# ----------------------------------------------------------------------
"""
Demonstrate the use of the argparse module.

usage: demoargs.py [-h] [-v]
                   {SJSU,Foothill,DeAnza,Berkeley} [players] [scale]
                   [scorefile]
positional arguments:
  {SJSU, Foothill, DeAnza, Berkeley}  What college will you play for?
  players              How many players?
  scale                What scale to use?
  scorefile            File to be used to save the score

optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        Print details?
"""
import argparse
import sys

def scale_type(entered_scale):
    """
    Validate the user entered scale and return the highest multiple
    of 10 that is less or equal to the entered scale
    :param entered_scale: (string)
    :return: integer
    """
    try:
        scale = float(entered_scale)
    except ValueError:
        raise argparse.ArgumentTypeError(f'invalid number')
    else:
        if scale < 10:
            raise argparse.ArgumentTypeError('must be >= 10')
    return int(scale) // 10 * 10


def get_arguments():
    """
    Parse and validate the command line arguments.
    :return: tuple containing the number of players (int),
        the scale(int), the college (string), scorefile (file object) 
        and the verbose option (boolean).
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('college',
                        help='What college will you play for?',
                        choices=['SJSU', 'Foothill', 'DeAnza', 'Berkeley'])

    parser.add_argument('players',
                        help='How many players?',
                        type=int,
                        nargs='?',
                        default=2)

    parser.add_argument('scale',
                        help='What scale to use?',
                        type=scale_type,
                        nargs='?',
                        default=10)

    parser.add_argument('scorefile',
                        help='File to be used to save the score',
                        type=argparse.FileType('x', encoding='UTF-8'),
                        nargs='?',
                        default=sys.stdout)

    parser.add_argument('-v', '--verbose',
                        help='Print details?',
                        action='store_true')

    arguments = parser.parse_args()
    players = arguments.players
    scale = arguments.scale
    college = arguments.college
    scorefile = arguments.scorefile
    verbose = arguments.verbose
    return players, scale, college, scorefile, verbose


def main():
    players, scale, college, scorefile, verbose = get_arguments()
    if verbose:
        print(f'Starting {college} game with {players} players')
        print(f'at a scale of {scale}.')
    scorefile.write('Hello\n')


if __name__ == '__main__':
    main()

