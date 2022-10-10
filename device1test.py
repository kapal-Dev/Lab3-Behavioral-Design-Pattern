
from devicetests import DeviceTest

class Device1Test(DeviceTest):

    def _mechanical_test(self):
        print("Device1, Mechanical test step1")
        print("Device1, Mechanical test step2")

    def _electric_test(self):
        print("Device1, Electric test step1")
        print("Device1, Electric test step2")
        print("Device1, Electric test step3")

    def _radio_test(self):
        print("Device1, Radio Test")

    def _audio_test(self):
        print("Device1, Audio Test")

    def _gather_results(self):
        print("Device1, gathering results")

    def _cleanup(self):
        print("Device1, cleaning up the results")

    def _create_summary(self):
        print("Device1, creating summary")

    def _print(self):
        print("Device1, creating test report")

