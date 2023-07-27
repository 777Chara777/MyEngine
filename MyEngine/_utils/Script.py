import sys
import os

from .._utils.BaseModule.LogError import logerror
from .._utils.BaseModule import BaseModule as bm

logerror.load_core("Engine")

_scripts: dict = {}

__all__ = (
    "Script",
    "ScriptCheck",
    "ScriptFile",
)

class ScriptFile:
    def __init__(self, _class) -> None:
        self.fun_class = _class

    def __str__(self) -> str:
        return "<ScriptFile class=%s>" % self.fun_class.__class__.__name__
    
    def __getattr__(self, item):
        return getattr(self.fun_class, item)

class ScriptFunctons(ScriptFile): pass

class ScriptCheck:
    def __init__(self, tag, core) -> None:
        self.__tag = tag
        self.__core = core

    def add_Script(self, class_):
        fun = class_(self.__core)
        _scripts[self.__tag] = ScriptFile(fun)

class Script:
    def __init__(self, core) -> None:
        logerror.info("__init__::Script")
        self._core = core

    @staticmethod
    def __len__():
        return len(_scripts)

    def getFunctions(self, tag: str) -> "ScriptFunctons | None":
        if tag in _scripts:
            return _scripts[tag]
        else:
            logerror.warn("this tag (%s) does not exist." % tag)

    def loadScripts(self, module: str, tag: str) -> "ScriptFile | None":
        if tag in _scripts:
            logerror.warn("This tag (%s) is already in use, please try another one." % tag)
            return
        
        path = os.path.abspath(module)
        module = path.split("\\")[-1].replace(".py", "")
        sys.path.append("/".join(path.split("\\")[:-1]))

        data = bm.initModule(module)
        if data["Type"]:
            data_module = data["Module"]
            data_module.setup(ScriptCheck(tag, self._core))

            return _scripts[tag]
        else:
            logerror.warn("loading module `%s` fail, because: %s" % (module, data["Message"]))


    def removeScript(self, tag: str):
        if tag in _scripts:
            logerror.info("removed script '%s'" % tag)
            del _scripts[tag]
        else:
            logerror.warn("cannot remove script '%s': script does not exist." % tag)

