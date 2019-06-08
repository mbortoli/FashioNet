from ipywidgets import widgets, Layout
from IPython.display import clear_output, display
from enum import Enum

__all__ = ['ImageLabeler', 'SelectionTypeEnum']

class SelectionTypeEnum(Enum):
    """
    Types allowed for label selection.
    """
    OPEN_FIELD = 1
    MULTIPLE = 2
    ONLY_ONE = 3

class ImageLabeler():
    """
    Displays images for labeling or deletion and saves them in `path` as 'labeled.csv'.
    Based on image_cleaner.py from fastai. 
    `https://github.com/fastai/fastai/blob/master/fastai/widgets/image_cleaner.py`
    """
    def __init__(self, path, batch_size:int=5, default_label:str='', label_options=[], selection_type:SelectionTypeEnum=SelectionTypeEnum.OPEN_FIELD):
        self._images_paths = [path + f for f in listdir(path)]
        self._batch_size = batch_size
        self._default_label = default_label
        self._label_options = label_options
        self._selection_type = selection_type
        self._csv_dict = dict()
        self.render()

    @classmethod
    def render(self):
        "Re-render Jupyter cell for batch of images."
        clear_output()
        self.write_csv()
        if self.empty():
            return display('No more images to label')
        else:
            display(self.make_horizontal_box(self.get_widgets(self._duplicates)))
            display(self.make_button_widget('Next Batch', handler=self.next_batch, style="primary"))
            
