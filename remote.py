#!/usr/bin/env python

import gtk
import telnetlib
import pygtk
pygtk.require('2.0')

class Table:

    def callback(self, widget, data):
	tn=telnetlib.Telnet("192.168.0.181",8080)
	print tn.read_until(">")
	tn.write(data + "\n")
	tn.close()

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("RokuRemote")
        self.window.connect("delete_event", self.delete_event)
        self.window.set_border_width(20)

        table = gtk.Table(7, 3, True)
        self.window.add(table)

	self.entry = gtk.Entry()

        button = gtk.Button("HOME")
        button.connect("clicked", self.callback, "press home")
        table.attach(button, 2, 3, 0, 2)
        button.show()

        button = gtk.Button("BACK")
        button.connect("clicked", self.callback, "press k")
        table.attach(button, 0, 1, 0, 2)
        button.show()

        button = gtk.Button("UP")
        button.connect("clicked", self.callback, "press up")
        table.attach(button, 1, 2, 1, 3)
        button.show()

        button = gtk.Button("SELECT")
        button.connect("clicked", self.callback, "press select")
        table.attach(button, 1, 2, 3, 5)
        button.show()

        button = gtk.Button("DOWN")
        button.connect("clicked", self.callback, "press down")
        table.attach(button, 1, 2, 5, 7)
        button.show()

        button = gtk.Button("LEFT")
        button.connect("clicked", self.callback, "press left")
        table.attach(button, 0, 1, 3, 5)
        button.show()

        button = gtk.Button("RIGHT")
        button.connect("clicked", self.callback, "press right")
        table.attach(button, 2, 3, 3, 5)
        button.show()

        button = gtk.Button("REPLAY")
        button.connect("clicked", self.callback, "press replay")
        table.attach(button, 0, 1, 6, 8)
        button.show()

        button = gtk.Button("INFO")
        button.connect("clicked", self.callback, "press info")
        table.attach(button, 2, 3, 6, 8)
        button.show()

        button = gtk.Button("II / >")
        button.connect("clicked", self.callback, "press pause")
        table.attach(button, 1, 2, 8, 10)
        button.show()

        button = gtk.Button("<<")
        button.connect("clicked", self.callback, "press back")
        table.attach(button, 0, 1, 8, 10)
        button.show()

        button = gtk.Button(">>")
        button.connect("clicked", self.callback, "press fwd")
        table.attach(button, 2, 3, 8, 10)
        button.show()

        table.show()

        self.window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    Table()
    main()
