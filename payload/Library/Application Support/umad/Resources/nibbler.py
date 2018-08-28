#!/usr/bin/python
# demo video here:
# https://www.dropbox.com/s/k0bpekd13muknmz/nibbler%20-%20by%20frogor.mp4?dl=0

# original gist here:
# https://gist.github.com/pudquick/f27efd1ddcbf57be0d14031a5e692015

# Example script using nibbler:

# from nibbler import *
#
# n = Nibbler('/Users/frogor/Desktop/sweet.nib')
#
# def test():
#     print "hi (no quit)"
#
# def test2():
#     print "hi (politely quit)"
#     n.quit()
#
# n.attach(test, 'pushy')
# n.attach(test2, 'less_pushy')
#
# n.hidden = True
# n.run()

# Use the "Identifier" property of your control in Interface Builder and give
# your controls a name. Then use the 'attach' method on your Nibbler to link
# the control to a python function

from Foundation import NSObject, NSBundle
from AppKit import NSNib, NSApp, NSApplication
import objc
import os
import os.path
import types

from ctypes import CDLL, Structure, POINTER, c_uint32, byref
from ctypes.util import find_library


class ProcessSerialNumber(Structure):
    _fields_ = [('highLongOfPSN', c_uint32), ('lowLongOfPSN',  c_uint32)]


kCurrentProcess = 2
kProcessTransformToForegroundApplication = 1
kProcessTransformToUIElementAppication = 4
ApplicationServices = CDLL(find_library('ApplicationServices'))
TransformProcessType = ApplicationServices.TransformProcessType
TransformProcessType.argtypes = [POINTER(ProcessSerialNumber), c_uint32]


def views_recursive(view_obj):
    yield view_obj
    for x in view_obj.subviews():
        for y in views_recursive(x):
            yield y


def views_dict(nib_obj):
    # Find the NSWindow instance at the top level
    all_windows = [x for x in nib_obj if x.className() == 'NSWindow']
    win = all_windows[0]
    # Now find all the views within the window where the identifier is defined
    top_view = win.contentView()
    v_dict = dict()
    for v in views_recursive(top_view):
        ident = v.identifier()
        if ident is not None:
            if not ident.startswith('_'):
                # Someone has customized it, remember it
                v_dict[ident] = v
    return v_dict


def quit_app():
    NSApplication.sharedApplication().terminate_(None)


class genericController(NSObject):
    def setTheThing_(self, f_obj):
        self.f = f_obj

    def doTheThing_(self, sender):
        if hasattr(self, 'f'):
            self.f()


def func_to_controller_selector(f_obj):
    o = genericController.alloc().init()
    o.setTheThing_(f_obj)
    return o


class Nibbler(object):
    def __init__(self, path):
        bundle = NSBundle.mainBundle()
        info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
        # Did you know you can override parts of infoDictionary (Info.plist,
        # after loading) even though Apple says it's read-only?
        info['LSUIElement'] = '1'
        # Initialize our shared application instance
        NSApplication.sharedApplication()
        # Two possibilities here
        # Either the path is a directory and we really want the file inside it
        # or the path is just a real .nib file
        if os.path.isdir(path):
            # Ok, so they just saved it from Xcode, not their fault
            # let's fix the path
            path = os.path.join(path, 'keyedobjects.nib')
        with open(path, 'rb') as f:
            # get nib bytes
            d = buffer(f.read())
        n_obj = NSNib.alloc().initWithNibData_bundle_(d, None)
        placeholder_obj = NSObject.alloc().init()
        result, n = n_obj.instantiateWithOwner_topLevelObjects_(
            placeholder_obj, None)
        self.hidden = True
        self.nib_contents = n
        self.win = [
            x for x in self.nib_contents if x.className() == 'NSWindow'][0]
        self.views = views_dict(self.nib_contents)
        self._attached = []

    def attach(self, func, identifier_label):
        # look up the object with the identifer provided
        o = self.views[identifier_label]
        # get the classname of the object and handle appropriately
        o_class = o.className()
        if o_class == 'NSButton':
            # Wow, we actually know how to do this one
            temp = func_to_controller_selector(func)
            # hold onto it
            self._attached.append(temp)
            o.setTarget_(temp)
            # button.setAction_(objc.selector(controller.buttonClicked_,
            # signature='v@:'))
            o.setAction_(temp.doTheThing_)

    def run(self):
        if self.hidden:
            psn = ProcessSerialNumber(0, kCurrentProcess)
            ApplicationServices.TransformProcessType(
                psn, kProcessTransformToUIElementAppication)
        else:
            psn = ProcessSerialNumber(0, kCurrentProcess)
            ApplicationServices.TransformProcessType(
                psn, kProcessTransformToForegroundApplication)
        self.win.makeKeyAndOrderFront_(None)
        self.win.display()
        NSApp.activateIgnoringOtherApps_(True)
        NSApp.run()

    def quit(self):
        NSApplication.sharedApplication().terminate_(None)
