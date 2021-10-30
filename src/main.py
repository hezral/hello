# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Adi Hezral <hezral@gmail.com>

import sys
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio

from .window import helloWindow


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='com.github.hezral.hello',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = helloWindow(application=self)
        win.present()


def main(version):
    app = Application()
    print(version)
    return app.run(sys.argv)
