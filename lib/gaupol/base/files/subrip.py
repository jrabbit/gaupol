# Copyright (C) 2005 Osmo Salomaa
#
# This file is part of Gaupol.
#
# Gaupol is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Gaupol is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Gaupol; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA


"""SubRip file."""


import codecs
import re

try:
    from psyco.classes import *
except ImportError:
    pass

from gaupol.constants import EXTENSION, FORMAT, MODE
from gaupol.base.files.subfile import SubtitleFile


class SubRip(SubtitleFile):
    
    """
    SubRip file.
    
    Subrip format quick reference:
    1
    00:00:18,176 --> 00:00:22,135
    And that completes my final report
    until we reach touchdown.
    
    2
    00:00:22,247 --> 00:00:26,046
    We're now on full automatic,
    in the hands of the computers.
    """

    ID_PATTERN = r'^\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d\s*$', None
    
    def __init__(self, *args):

        SubtitleFile.__init__(self, *args)

        self.FORMAT    = FORMAT.SUBRIP
        self.EXTENSION = EXTENSION.SUBRIP
        self.MODE      = MODE.TIME

    def read(self):
        """
        Read Subrip file.

        Raise IOError if reading fails.
        Raise UnicodeError if decoding fails.
        Return show times, hide times, texts.
        """
        # Compile regular expressions.
        re_blank_line = re.compile(r'^\s*$')
        time = r'\d\d:\d\d:\d\d,\d\d\d'
        re_time_line = re.compile(r'^(%s) --> (%s)\s*$' % (time, time))
        
        lines = self._read_lines()
        good_lines = []
        
        # Remove blank lines and unit numbers.
        for line in lines:

            if re_blank_line.match(line) is not None:
                continue
            elif re_time_line.match(line) is not None:
                good_lines[-1] = line
            else:
                good_lines.append(line)

        shows = []
        hides = []
        texts = []
        
        # Split to components.
        for line in good_lines:
        
            match = re_time_line.match(line)
            
            if match is not None:
                shows.append(match.group(1))
                hides.append(match.group(2))
                texts.append(u'')
            else:
                texts[-1] += line

        # Remove leading and trailing spaces.
        self._strip_spaces(texts)

        return shows, hides, texts

    def write(self, shows, hides, texts):
        """
        Write SubRip file.

        Raise IOError if writing fails.
        Raise UnicodeError if encoding fails.
        """
        newline_character = self._get_newline_character()

        # Replace python internal newline characters in text with desired
        # newline characters.
        texts = [text.replace('\n', newline_character) for text in texts]

        subtitle_file = codecs.open(self.path, 'w', self.encoding)

        try:
            for i in range(len(shows)):
                subtitle_file.write('%.0f%s%s --> %s%s%s%s%s' % (
                    i + 1, newline_character,
                    shows[i], hides[i], newline_character,
                    texts[i], newline_character, newline_character
                ))
        finally:
            subtitle_file.close()
