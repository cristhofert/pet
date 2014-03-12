#!/usr/bin/env python

import glucosa
import gtk
import gobject

HUNGER = 0

class Game(glucosa.GameArea):

    def __init__(self):
        glucosa.GameArea.__init__(self)

        print 'Loading'

        _events = glucosa.Events(self)
        _pet = Pet()
        self.mouth = Mouth()
        self.peach = Food('banana.png', 0, 0, self.mouth)
        
        self.connect('draw', _pet._update)
        self.connect('draw', self.mouth._update)
        self.connect('draw', self.update)
        _events.connect('mouse-moved', self.mouth.move)
        _events.connect('mouse-moved', self.peach.move)
        _events.connect('mouse-button-pressed', self.peach.click_pressed)
        _events.connect('mouse-button-released', self.peach.click_released)

        self.add_sprite(_pet)
        self.add_sprite(self.mouth)
        self.add_sprite(self.peach)

        print 'starting'

    def update(self, widget, data):
        if self.peach.collision_with(self.mouth):
            self.peach.kill()

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
    def __init__(self, image, _x, _y, mouth):
        self.start_pos = _x, _y
        _image = glucosa.Image('images/' + image)
        glucosa.Sprite.__init__(self, _image, *self.start_pos)

        self._to_rotate = 0
        self.follow = False


    def _update(self, widget, event):
        pass
        
    def move(self, widget, data):
        lr =  data['x'] > self.get_left() and  data['x'] > self.get_left()
        tb = data['y'] > self.get_top() and data['y'] < self.get_bottom() + 100
        a = lr and tb
        if a:
            self.set_scale(1.1)
        else:
            self.set_scale(1)

        if self.follow:
            self.set_pos(data['x'], data['y'])
            
    def click_pressed(self, widget, data):
        #self.set_pos(data['x'], data['y'])
        self.follow = True

    def click_released(self, widget, data):
        #self.set_pos(data['x'], data['y'])
        self.follow = False

    def kill(self):
        self.set_pos(0, 0)
        
if __name__ == '__main__':
    w = gtk.Window()
    w.maximize()
    w.connect('destroy', gtk.main_quit)
    w.add(Game())
    w.show_all()
    gtk.main()
