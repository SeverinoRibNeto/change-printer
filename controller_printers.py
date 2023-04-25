from pubsub import pub


class PrinterController:
    def __init__(self) -> None:
        pub.subscribe(self.saveConfig, "Save_Config_Pressed")
        pub.subscribe(self.loadConfig, "Load_Config_Pressed")
        pub.subscribe(self.start, "Start_Pressed")
        return

    def saveConfig(self) -> None:
        pass

    def loadConfig(self) -> None:
        pass

    def start(self) -> None:
        pass
