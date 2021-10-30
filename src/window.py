# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2021 Adi Hezral <hezral@gmail.com>

import gi
gi.require_version('Handy', '1')
gi.require_version('Granite', '1.0')
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, Handy, Gdk, Gio, WebKit2, GLib, cairo, Granite

class helloWindow(Handy.ApplicationWindow):
    __gtype_name__ = 'helloWindow'

    Handy.init()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        header = Handy.HeaderBar()
        header.props.show_close_button = True
        header.props.hexpand = True
        header.props.title = "hello World"

        label = Gtk.Label("hello World")
        label.props.expand = True
        label.props.valign = label.props.halign = Gtk.Align.CENTER

        self.grid = Gtk.Grid()
        self.grid.props.expand = True
        self.grid.attach(header, 0, 0, 1, 1)
        self.grid.attach(label, 0, 1, 1, 1)
        self.grid.connect("button-press-event", self.on_button_press)

        window_handle = Handy.WindowHandle() 
        window_handle.add(self.grid)

        self.add(window_handle)
        self.props.default_width = 480
        self.props.default_height = 320
        self.show_all()

        self.window_menu = Gtk.Menu()
        screenshot = Gtk.MenuItem()
        screenshot_accellabel = Granite.AccelLabel(label="Take Screenshot")
        screenshot.add(screenshot_accellabel)
        self.window_menu.append(screenshot)
        self.window_menu.show_all()

    def on_button_press(self, windowhandle, eventbutton):

        print(eventbutton.button)
        if eventbutton.button == 1:
            self.window_menu.popup_at_pointer()
        
