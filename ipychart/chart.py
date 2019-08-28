import ipywidgets as widgets
from traitlets import Unicode, default, List


class Chart(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('ChartView').tag(sync=True)
    _model_name = Unicode('ChartModel').tag(sync=True)
    _view_module = Unicode('ipychart').tag(sync=True)
    _model_module = Unicode('ipychart').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)

    _data = List([]).tag(sync=True)
    _label = List([]).tag(sync=True)

    _type = Unicode().tag(sync=True)

    def __init__(self, data, kind):
        super().__init__()
        assert kind in ['line', 'bar', 'horizontalBar', 'radar', 'doughnut', 'polarArea',
                        'bubble', 'pie'], 'Type must be one of : line, bar, radar, doughnut, polarArea, bubble'
        assert isinstance(data, (list, dict)), 'Please enter data as dict of list'

        if isinstance(data, list):
            self._data = data
            self._label = [str(i + 1) for i in range(len(self._data))]

        else:
            assert 'data' in data, 'Please input data using the key "data" in the dict'
            if 'labels' in data:
                assert len(data['labels']) == len(data['data'])

            self._data = data['data'] if 'data' in data else None
            self._label = data['labels'] if 'labels' in data else [str(i + 1) for i in range(len(self._data))]

        self._type = kind

    @default('layout')
    def _default_layout(self):
        return widgets.Layout(height='auto', align_self='stretch')
