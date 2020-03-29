#!/usr/bin/python3

import os
import random
import subprocess


class Wallpaper():
    def __init__(self,
                 bg_file_dir='.',
                 bg_file_ext=('.jpg', '.png'),
                 lock_bin='/usr/bin/betterlockscreen',
                 lock_bin_flags='-u',
                 recursive=False):
        self.bg_file_dir = bg_file_dir
        self.bg_file_ext = bg_file_ext
        self.lock_bin = lock_bin
        self.lock_bin_flags = lock_bin_flags
        self.recursive = recursive

        self.bg_list = []

    def rnd_bg(self):
        for root, dirs, files in os.walk(self.bg_file_dir):
            for fn in files:
                if fn.endswith((self.bg_file_ext)):
                    self.bg_list += [fn]
            if self.recursive == False:
                break

        if len(self.bg_list) < 1:
            raise (
                'No wallpapers matching specified file extensions in specified directory.'
            )

        rnd_idx = random.randint(1, len(self.bg_list))
        rnd_bg = os.path.join(self.bg_file_dir, self.bg_list[rnd_idx])

        return rnd_bg

    def set_bg(self):
        FNULL = open(os.devnull, 'w')

        subprocess.call(
            [self.lock_bin, self.lock_bin_flags,
             self.rnd_bg()],
            stdout=FNULL,
            stderr=subprocess.STDOUT)


def main():
    w = Wallpaper(bg_file_dir='/home/ws/images/bg/.')
    w.set_bg()


if __name__ == '__main__':
    main()
