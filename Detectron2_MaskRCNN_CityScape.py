from ikomia import dataprocess
import Detectron2_MaskRCNN_CityScape_process as processMod
import Detectron2_MaskRCNN_CityScape_widget as widgetMod


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class Detectron2_MaskRCNN_CityScape(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        # Instantiate process object
        return processMod.Detectron2_MaskRCNN_CityScapeProcessFactory()

    def getWidgetFactory(self):
        # Instantiate associated widget object
        return widgetMod.Detectron2_MaskRCNN_CityScapeWidgetFactory()
