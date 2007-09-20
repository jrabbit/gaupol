[application_window]
maximized = boolean(default=False)
position = int_list(2, 2, default=list(0, 0))
show_main_toolbar = boolean(default=True)
show_statusbar = boolean(default=True)
show_video_toolbar = boolean(default=False)
size = int_list(2, 2, default=list(600, 371))
toolbar_style = TOOLBAR_STYLE(default="DEFAULT")

[common_error]
country = string(default=None)
human = boolean(default=True)
language = string(default=None)
ocr = boolean(default=True)
script = string(default="Latn")

[debug]
editor = string(default="gedit")

[duration_adjust]
gap = float(min=0.0, default=0.0)
lengthen = boolean(default=True)
maximum = float(min=0.0, default=6.0)
minimum = float(min=0.0, default=1.5)
optimal = float(min=0.0, default=0.065)
shorten = boolean(default=False)
target = TARGET(default="CURRENT")
use_gap = boolean(default=True)
use_maximum = boolean(default=False)
use_minimum = boolean(default=True)

[editor]
custom_font = string(default=None)
framerate = FRAMERATE(default="P24")
length_unit = LENGTH_UNIT(default="EM")
limit_undo = boolean(default=False)
mode = MODE(default="TIME")
show_lengths_cell = boolean(default=True)
show_lengths_edit = boolean(default=True)
undo_levels = integer(min=0, default=50)
use_custom_font = boolean(default=False)
visible_columns = COLUMN_list(default=list("NUMBER", "START", "END", "DURATION", "MAIN_TEXT"))

[encoding]
fallbacks = string_list(default=list("utf_8", "cp1252"))
try_auto = boolean(default=True)
try_locale = boolean(default=True)
visibles = string_list(default=list("utf_8", "cp1252"))

[file]
directory = string(default=None)
encoding = string(default=None)
format = FORMAT(default="SUBRIP")
max_recent = integer(min=0, default=10)
newline = NEWLINE(default="UNIX")
smart_open_translation = boolean(default=True)
warn_ssa = boolean(default=True)

[framerate_convert]
target = TARGET(default="CURRENT")

[general]
version = string(default=None)

[hearing_impaired]
country = string(default=None)
language = string(default=None)
script = string(default="Latn")

[line_break]
country = string(default=None)
language = string(default=None)
length_unit = LENGTH_UNIT(default="EM")
max_deviation = float(default=0.16)
max_length = integer(min=1, default=29)
max_lines = integer(min=1, default=2)
max_skip_length = integer(min=1, default=29)
max_skip_lines = integer(min=1, default=3)
script = string(default="Latn")
skip_length = boolean(default=True)
skip_lines = boolean(default=True)

[output_window]
maximized = boolean(default=False)
position = int_list(2, 2, default=list(0, 0))
show = boolean(default=False)
size = int_list(2, 2, default=list(600, 371))

[position_shift]
target = TARGET(default="CURRENT")

[position_transform]
target = TARGET(default="CURRENT")

[preview]
custom_command = string(default=None)
offset = float(default=5.0)
use_custom = boolean(default=False)
video_player = VIDEO_PLAYER(default="MPLAYER")

[search]
columns = COLUMN_list(default=list("MAIN_TEXT"))
ignore_case = boolean(default=True)
max_history = integer(min=0, default=10)
regex = boolean(default=False)
target = TARGET(default="CURRENT")

[spell_check]
column = COLUMN(default="MAIN_TEXT")
language = string(default="en")
target = TARGET(default="CURRENT")

[subtitle_insert]
above = boolean(default=False)

[text_assistant]
column = COLUMN(default="MAIN_TEXT")
pages = string_list(default=list())
remove_blank = boolean(default=True)
target = TARGET(default="CURRENT")