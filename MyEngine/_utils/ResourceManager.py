from .._utils.BaseModule.LogError import logerror

logerror.load_core("Engine")

class ResorseManager:
    def __init__(self) -> None:
        logerror.info("__init__ ResorseManager")
