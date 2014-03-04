#!/usr/bin/env python

import glucosa
import gtk
import gobject


class Game(glucosa.GameArea):

    def __init__(self):
        glucosa.GameArea.__init__(self)

        _events = glucosa.Events(self)
        _pet = Pet()
        mouth = Mouth()
        banana = Food('banana.png')
        
        self.connect('draw', _pet._update)
        self.connect('draw', mouth._update)
        _events.connect('mouse-moved', mouth.move)
        _events.connect('mouse-moved', banana.move)


        self.add_sprite(_pet)
        self.add_sprite(mouth)
        self.add_sprite(banana)


class Pet(glucosa.Sprite):
    def __init__(self):
        _image = glucosa.Image('images/pet.png')
        glucosa.Sprite.__init__(self, _image, 400, 100)

        self._to_rotate = 0

    def _update(self, widget, event):
        pass

class Mouth(glucosa.Sprite):
    def __init__(self):
        self._image = glucosa.Image('images/mouth.png')
        self._image2 = glucosa.Image('images/mouth2.png')
        glucosa.Sprite.__init__(self, self._image, 550, 400)

    def _update(self, widget, event):
        pass

    def move(self, widget, data):
        lr =  data['x'] > self.get_left() and  data['x'] > self.get_left()
        tb = data['y'] > self.get_top() and data['y'] < self.get_bottom() + 100
        a = lr and tb
        if a:
            self.set_image(self._image2)
        else:
            self.set_image(self._image)
    
class Food(glucosa.Sprite):
    def __init__(self, image):
        _image = glucosa.Image(image)
        glucosa.Sprite.__init__(self, _image, 400, 100)

        self._to_rotate = 0

    def _update(self, widget, event):
        pass

    def move(self, widget, data):
        lr =  data['x'] > self.get_left() and  data['x'] > self.get_left()
        tb = data['y'] > self.get_top() and data['y'] < self.get_bottom() + 100
        a = lr and tb
        if a:
            self.set_scale(2)
        else:
            self.set_scale(1)

if __name__ == '__main__':
    w = gtk.Window()
    w.maximize()
    w.connect('destroy', gtk.main_quit)
    w.add(Game())
    w.show_all()
    gtk.main()
