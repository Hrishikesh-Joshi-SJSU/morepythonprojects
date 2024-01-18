# ----------------------------------------------------------------------
# Name:        matchit
# Purpose:     Implement a single player matching game
#
# Author(s): Hrishikesh Joshi and Paul Chon
# ----------------------------------------------------------------------
"""
A single player matching game.

usage: matchit.py [-h] [-f] {blue,green,magenta} [image_folder]

positional arguments:
  {blue,green,magenta} What color would you like for the player?
  image_folder What folder contains the game images?

optional arguments:
  -h, --help show this help message and exit
  -f, --fast Fast or slow game?
"""
import tkinter
import os
import random
import argparse


class MatchGame(object):
    """
    GUI Game class for a matching game.

    Arguments:
    parent: the root window object
    player_color (string): the color to be used for the matched tiles
    folder (string): the folder containing the images for the game
    delay (integer): how many milliseconds to wait before flipping a tile

    Attributes:
    Please list ALL the instance variables here
    score (int): the player's score
    tries (int): number of matching attempts
    matches (int): number of pairs of matched tiles
    image_names (list): of image names in the game
    image_dict (dict): of image names corresponding to a PhotoImage
    folder (str): image folder
    player_color: (string) the color for the matched tiles
    delay (int): how many milliseconds to wait before flipping a tile
    canvas (tkinter.Canvas): the widget defining the area to be painted
    restart_button (tkinter.Button): button to restart the game at any
    point
    score_message (tkinter.Label): label to display the current score
    game_over (tkinter.Label): label to display the game over message
    tries_message (tkinter.Label): label to display the number of tries
    """
    # Add your class variables if needed here - square size, etc...)
    image_names = None
    size = 600
    width = size / 4
    height = size / 4
    tile_color = 'yellow'

    def __init__(self, parent, player_color, folder, delay):
        self.score = 100
        self.tries = 0
        self.matches = 0
        self.image_names = None
        self.image_dict = None
        self.folder = folder
        self.player_color = player_color
        self.delay = delay

        parent.title('Match it!')
        self.restart_button = tkinter.Button(parent, text='RESTART',
                                             command=self.restart)
        self.restart_button.grid()

        self.canvas = tkinter.Canvas(parent, height=self.size, width=self.size)
        self.canvas.grid()

        self.score_message = tkinter.Label(parent, text=f'Score: {self.score}')
        self.game_over = tkinter.Label(parent, text='')
        self.tries_message = tkinter.Label(parent, text='')

        self.create_tiles()
        self.canvas.grid()
        self.canvas.bind("<Button-1>", self.flip)

        self.game_over.grid()
        self.score_message.grid()
        self.tries_message.grid()
        self.restart()

    def restart(self):
        """
        This method is invoked when player clicks on the RESTART button.
        It should also be called from __init__ to initialize the game.
        It shuffles and reassigns the images and resets the GUI and the
        score.
        :return: None
        """
        self.score = 100
        self.tries = 0
        self.matches = 0
        self.score_message.configure(text=f'Score: {self.score}')
        self.game_over.configure(text='')
        self.tries_message.configure(text=f'')
        self.create_tiles()

    def flip(self, event):
        """
        This method is invoked when the user clicks on a square.
        It implements the basic controls of the game.
        :param event: event (Event object) describing the click event
        :return: None
        """
        if 'image' in self.canvas.gettags(tkinter.CURRENT) or \
                self.canvas.itemcget(tkinter.CURRENT, 'fill') == \
                self.player_color or self.canvas.gettags('second'):
            return

        self.canvas.itemconfigure(tkinter.CURRENT, fill=self.player_color)

        current_tags = self.canvas.gettags(tkinter.CURRENT)
        x1, y1, x2, y2 = self.canvas.coords(tkinter.CURRENT)
        self.canvas.create_image(x1 + self.width / 2, y1 + self.width / 2,
                                 image=self.image_dict[current_tags[0]],
                                 tags='image')

        if not self.canvas.gettags('first'):
            self.canvas.addtag_withtag('first', tkinter.CURRENT)
        else:
            self.canvas.addtag_withtag('second', tkinter.CURRENT)
            self.canvas.after(self.delay, self.hide)
            self.tries += 1

    def hide(self):
        """
        This method is called after a delay to hide the two tiles that
        were flipped.  The method will also change the tile color to the
        user specified color if there is a match.
        :return: None
        """
        first_tags = self.canvas.gettags('first')
        second_tags = self.canvas.gettags('second')
        if first_tags[0] != second_tags[0]:
            self.canvas.itemconfigure('first', fill=self.tile_color)
            self.canvas.itemconfigure('second', fill=self.tile_color)
        else:
            self.matches += 1

        if self.tries > 13:
            self.score -= 10
            self.score_message.configure(text=f'Score: {self.score}')

        if self.matches == 8:
            self.game_over.configure(text='Game over!')
            self.tries_message.configure(text=f'Number of tries: {self.tries}')
        self.canvas.delete('image')
        self.canvas.dtag('first', 'first')
        self.canvas.dtag('second', 'second')

    def create_tiles(self):
        """
        Creates the tiles for the game also shuffles and associates the
        tiles with their respective images
        :return: None
        """
        self.image_names = MatchGame.image_names * 2
        random.shuffle(self.image_names)
        self.image_dict = {name: tkinter.PhotoImage(file=f'{self.folder}'
                                                         f'/{name}')
                           for name in MatchGame.image_names[0:8] if
                           os.path.splitext(name)[1] == '.gif'}

        tiles = []
        for row in range(4):
            for col in range(4):
                tile = self.canvas.create_rectangle(col * self.width,
                                                    row * self.height,
                                                    (col + 1) * self.width,
                                                    (row + 1) * self.height,
                                                    fill=self.tile_color)

                tiles.append(tile)

        for i in range(len(tiles)):
            self.canvas.itemconfigure(tiles[i], tags=self.image_names[i])


def validate_folder(folder):
    """
    Validate the image_folder argument that it exists and has at least
    8 gif images
    :param folder: image_folder argument
    :return: validated folder
    """
    if os.path.exists(folder):
        file_contents = os.listdir(folder)
        MatchGame.image_names = [file for file in os.listdir(folder)
                                 if os.path.splitext(file)[1] == '.gif'][
                                0:8]
        # gif_counter = 0
        # for image in file_contents:
        #     file_name, ext = os.path.splitext(image)
        #     if ext == '.gif':
        #         gif_counter += 1
        # if gif_counter < 8:
        #     raise argparse.ArgumentTypeError(f'{folder} must contain '
        #                                      f'at least 8 gif images')
        if len(MatchGame.image_names) < 8:
            raise argparse.ArgumentTypeError(f'{folder} must contain '
                                             f'at least 8 gif images')
        return folder
    else:
        raise argparse.ArgumentTypeError(f'{folder} is not a valid folder')


def get_arguments():
    """
    Parse and validate the command line arguments.
    :return: tuple containing the player color (string), the image
    folder (string) and the fast option (boolean)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('color',
                        help='What color would you like for the player?',
                        choices=['blue', 'green', 'magenta'])

    parser.add_argument('image_folder',
                        help='What folder contains the game images?',
                        type=validate_folder,
                        nargs='?',
                        default="images")

    parser.add_argument('-f', '--fast',
                        help='Fast game or slow game?',
                        action='store_true')
    arguments = parser.parse_args()
    color = arguments.color
    image_folder = arguments.image_folder
    fast = arguments.fast

    return color, image_folder, fast


def main():
    delay = 3000
    color, image_folder, fast = get_arguments()
    if fast:
        delay = 1000
    root = tkinter.Tk()
    game = MatchGame(root, color, image_folder, delay)
    root.mainloop()
    # Retrieve and validate the command line arguments using argparse
    # Instantiate a root window
    # Instantiate a MatchGame object with the correct arguments
    # Enter the main event loop


if __name__ == '__main__':
    main()