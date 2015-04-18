# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_rpi_ws281x', [dirname(__file__)])
        except ImportError:
            import _rpi_ws281x
            return _rpi_ws281x
        if fp is not None:
            try:
                _mod = imp.load_module('_rpi_ws281x', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _rpi_ws281x = swig_import_helper()
    del swig_import_helper
else:
    import _rpi_ws281x
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


WS2811_TARGET_FREQ = _rpi_ws281x.WS2811_TARGET_FREQ
class ws2811_channel_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ws2811_channel_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ws2811_channel_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["gpionum"] = _rpi_ws281x.ws2811_channel_t_gpionum_set
    __swig_getmethods__["gpionum"] = _rpi_ws281x.ws2811_channel_t_gpionum_get
    if _newclass:gpionum = _swig_property(_rpi_ws281x.ws2811_channel_t_gpionum_get, _rpi_ws281x.ws2811_channel_t_gpionum_set)
    __swig_setmethods__["invert"] = _rpi_ws281x.ws2811_channel_t_invert_set
    __swig_getmethods__["invert"] = _rpi_ws281x.ws2811_channel_t_invert_get
    if _newclass:invert = _swig_property(_rpi_ws281x.ws2811_channel_t_invert_get, _rpi_ws281x.ws2811_channel_t_invert_set)
    __swig_setmethods__["count"] = _rpi_ws281x.ws2811_channel_t_count_set
    __swig_getmethods__["count"] = _rpi_ws281x.ws2811_channel_t_count_get
    if _newclass:count = _swig_property(_rpi_ws281x.ws2811_channel_t_count_get, _rpi_ws281x.ws2811_channel_t_count_set)
    __swig_setmethods__["brightness"] = _rpi_ws281x.ws2811_channel_t_brightness_set
    __swig_getmethods__["brightness"] = _rpi_ws281x.ws2811_channel_t_brightness_get
    if _newclass:brightness = _swig_property(_rpi_ws281x.ws2811_channel_t_brightness_get, _rpi_ws281x.ws2811_channel_t_brightness_set)
    __swig_setmethods__["leds"] = _rpi_ws281x.ws2811_channel_t_leds_set
    __swig_getmethods__["leds"] = _rpi_ws281x.ws2811_channel_t_leds_get
    if _newclass:leds = _swig_property(_rpi_ws281x.ws2811_channel_t_leds_get, _rpi_ws281x.ws2811_channel_t_leds_set)
    def __init__(self): 
        this = _rpi_ws281x.new_ws2811_channel_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _rpi_ws281x.delete_ws2811_channel_t
    __del__ = lambda self : None;
ws2811_channel_t_swigregister = _rpi_ws281x.ws2811_channel_t_swigregister
ws2811_channel_t_swigregister(ws2811_channel_t)

class ws2811_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ws2811_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ws2811_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["device"] = _rpi_ws281x.ws2811_t_device_set
    __swig_getmethods__["device"] = _rpi_ws281x.ws2811_t_device_get
    if _newclass:device = _swig_property(_rpi_ws281x.ws2811_t_device_get, _rpi_ws281x.ws2811_t_device_set)
    __swig_setmethods__["freq"] = _rpi_ws281x.ws2811_t_freq_set
    __swig_getmethods__["freq"] = _rpi_ws281x.ws2811_t_freq_get
    if _newclass:freq = _swig_property(_rpi_ws281x.ws2811_t_freq_get, _rpi_ws281x.ws2811_t_freq_set)
    __swig_setmethods__["dmanum"] = _rpi_ws281x.ws2811_t_dmanum_set
    __swig_getmethods__["dmanum"] = _rpi_ws281x.ws2811_t_dmanum_get
    if _newclass:dmanum = _swig_property(_rpi_ws281x.ws2811_t_dmanum_get, _rpi_ws281x.ws2811_t_dmanum_set)
    __swig_setmethods__["channel"] = _rpi_ws281x.ws2811_t_channel_set
    __swig_getmethods__["channel"] = _rpi_ws281x.ws2811_t_channel_get
    if _newclass:channel = _swig_property(_rpi_ws281x.ws2811_t_channel_get, _rpi_ws281x.ws2811_t_channel_set)
    def __init__(self): 
        this = _rpi_ws281x.new_ws2811_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _rpi_ws281x.delete_ws2811_t
    __del__ = lambda self : None;
ws2811_t_swigregister = _rpi_ws281x.ws2811_t_swigregister
ws2811_t_swigregister(ws2811_t)


def ws2811_init(*args):
  return _rpi_ws281x.ws2811_init(*args)
ws2811_init = _rpi_ws281x.ws2811_init

def ws2811_fini(*args):
  return _rpi_ws281x.ws2811_fini(*args)
ws2811_fini = _rpi_ws281x.ws2811_fini

def ws2811_render(*args):
  return _rpi_ws281x.ws2811_render(*args)
ws2811_render = _rpi_ws281x.ws2811_render

def ws2811_wait(*args):
  return _rpi_ws281x.ws2811_wait(*args)
ws2811_wait = _rpi_ws281x.ws2811_wait

def ws2811_led_get(*args):
  return _rpi_ws281x.ws2811_led_get(*args)
ws2811_led_get = _rpi_ws281x.ws2811_led_get

def ws2811_led_set(*args):
  return _rpi_ws281x.ws2811_led_set(*args)
ws2811_led_set = _rpi_ws281x.ws2811_led_set

def ws2811_channel_get(*args):
  return _rpi_ws281x.ws2811_channel_get(*args)
ws2811_channel_get = _rpi_ws281x.ws2811_channel_get
# This file is compatible with both classic and new-style classes.


