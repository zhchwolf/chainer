class OnceTrigger(object):

    """Trigger based on the starting point of the iteration.

    This trigger accepts only once at starting point of the iteration. There
    are two ways to specify the starting point: only starting point in whole
    iteration or called again when training resumed.

    Args:
        call_on_resume (bool): Whether the extension is called again or not
            when restored from a snapshot. It is set to ``False`` by default.

    Attributes:
        finished (bool): Flag that triggered when this trigger called once.
            The flag helps decision to call `Extension.initialize` or not
            in `trainer`.
    """

    def __init__(self, call_on_resume=False):
        self._flag_first = True
        self._flag_resumed = call_on_resume

    def trigger(self, trainer):
        flag = not self.finished
        self._flag_resumed = False
        self._flag_first = False
        return flag

    @property
    def finished(self):
        return not (self._flag_first or self._flag_resumed)

    def serialize(self, serializer):
        self._flag_first = serializer('_flag_first', self._flag_first)
