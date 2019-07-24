""" Transparent, irregular edge splash screen with pyGTK and XShape.
Takes a png image with transparent section, creates a window with pyGTK, puts this image in
there with cairo and then trims the edges with X11 XShape clipping extension.
This file demonstrates a python script which loads a png image of size 800x650 and name base.png
Then it creates a GTK+/Cairo window with opaque settings from the png file and the transparent
portions cut out with a mask. Basic, but works and looks great.
Note: this is a proof of concept file. It works, but it is by no means production ready.
"""

import sys
import os
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk, Gdk, GObject
import cairo
import gobject

class TransparentWindow(Gtk.Window):
    def __init__(self, filename):
        Gtk.Window.__init__(self)

        self.set_size_request(300, 220)
        self.set_keep_above(True)

        # pasang event delete, biar bisa di close
        self.connect('destroy', Gtk.main_quit)
        ### agar border window terlihat/tidak terlihat (0=hidden/1=shown), origin=0
        self.set_decorated(0)
        self.move(0,0)

        # bikin transparan
        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        # make window transparent
        if visual and screen.is_composited():
            self.set_visual(visual)

        # define widget content
        self.entry = Gtk.Entry()
        # tambah gambar
        image = Gtk.Image()
        image.set_from_file(filename)
        # dengarkan event
        self.entry.connect('key_release_event', self.on_key_press)

        # tambah widget
        box = Gtk.VBox()
        entry_box = Gtk.HBox()
        entry_box.show()

        box.pack_start(image,  expand = False, fill = False, padding = 0)
        box.pack_start(entry_box,  expand = False, fill = False, padding = 0)
        entry_box.pack_start(self.entry,  expand = False, fill = False, padding = 0)
        self.add(box)

        self.set_app_paintable(True)
        # display window
        self.show_all()

    # get text on enter
    def on_key_press(self, widget, event):
        # print("      Key val, name: ", event.keyval, Gdk.keyval_name(event.keyval))
        keypress = Gdk.keyval_name(event.keyval)
        user_input = self.entry.get_text()
        if keypress == 'Return':
            self.destroy()
            self.result = user_input
            print(user_input)

    # biar ga langsung ke close
    def hold(self):
        Gtk.main()

    def quit(self):
        Gtk.main_quit()
        return False

if __name__ == "__main__":
    filename="/home/pulpen/Pictures/bot/hello-fusion.png"
    if len(sys.argv) > 1:
        if sys.argv[1] == "hello":
            filename="/home/pulpen/Pictures/bot/hello-fusion.png"
        elif sys.argv[1] == "abis":
            filename="/home/pulpen/Pictures/bot/abis-fusion.png"
        elif sys.argv[1] == "penuh":
            filename="/home/pulpen/Pictures/bot/penuh-fusion.png"
        elif sys.argv[1] == "pre_solat":
            filename="/home/pulpen/Pictures/bot/pre-solat-fusion.png"
        elif sys.argv[1] == "solat":
            filename="/home/pulpen/Pictures/bot/solat-fusion.png"
        elif sys.argv[1] == "ingetin_minum":
            filename="/home/pulpen/Pictures/bot/minum-fusion.png"
        else :
            filename=sys.argv[1]
    # spawn transparent window
    TransparentWindow(filename)
    # start processing loop biar ga langsung ke close
    Gtk.main()
