General Information
===================

Gaupol is an editor for text-based subtitle files. It supports multiple
subtitle file formats and provides means of creating subtitles, editing
texts and timing subtitles to match video. The user interface is
designed with attention to batch processing of multiple documents and
convenience of translating.

Gaupol contains aeidon, a separately installable general-purpose
Python package for reading, writing and manipulating text-based
subtitle files. See the file `README.aeidon.md` for details.

Gaupol is free software released under the GNU General Public License
(GPL), see the file `COPYING` for details.

Dependencies
============

Gaupol requires [Python][1] 3.2 or greater, [PyGObject][2] 3.6.0 or
greater and [GTK+][3] 3.2 or greater. Optional, but strongly recommended
dependencies follow.

 * [GStreamer][4] 1.0 or greater (at least the core, gst-plugins-base
   and gst-plugins-good; and for good container and codec support
   preferrably each of gst-plugins-bad, gst-plugins-ugly and gst-libav)
   -- required for the integrated video player
 * [PyEnchant][5] 1.4.0 or greater -- required for spell-checking
 * [GtkSpell][6] 3.0.0 or greater -- required for inline spell-checking
 * [iso-codes][7] -- required to translate language and country names
 * [Universal Encoding Detector][8] (a.k.a. chardet) -- required for
   character encoding auto-detection
 * [MPlayer][9] or [VLC][10] -- recommended for preview
 * [PT Sans Caption and PT Mono fonts][11] -- recommended and used by
   default for integrated video player's subtitle and timecode overlays

  [1]: http://www.python.org/
  [2]: http://wiki.gnome.org/Projects/PyGObject
  [3]: http://www.gtk.org/
  [4]: http://gstreamer.freedesktop.org/
  [5]: http://pythonhosted.org/pyenchant/
  [6]: http://gtkspell.sourceforge.net/
  [7]: http://pkg-isocodes.alioth.debian.org/
  [8]: http://pypi.python.org/pypi/chardet
  [9]: http://www.mplayerhq.hu/
 [10]: http://www.videolan.org/vlc/
 [11]: http://www.paratype.com/public/

Running
=======

To try Gaupol from the source directory without installation, use
command `python3 bin/gaupol`. For installing Gaupol, see the file
`INSTALL.md`.