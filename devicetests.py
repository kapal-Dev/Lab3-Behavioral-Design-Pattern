from abc import abstractmethod, ABCMeta



class DeviceTest(metaclass=ABCMeta):

    def test(self):
        self._electric_test()
        self._mechanical_test()
        self._radio_test()
        self._audio_test()

    def create_report(self):
        self._gather_results()
        self._cleanup()
        self._create_summary()
        self._print()

    @abstractmethod
    def _electric_test(self):
        pass

    @abstractmethod
    def _mechanical_test(self):
        pass

    @abstractmethod
    def _radio_test(self):
        pass

    @abstractmethod
    def _audio_test(self):
        pass

    @abstractmethod
    def _gather_results(self):
        pass

    @abstractmethod
    def _cleanup(self):
        pass

    @abstractmethod
    def _create_summary(self):
        pass

    @abstractmethod
    def _print(self):
        pass
    


