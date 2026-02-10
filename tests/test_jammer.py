import unittest,sys,os
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"..","src"))
from nullsec_payload_wifijammer.core import JammerDetector

class TestJammer(unittest.TestCase):
    def test_baseline(self):
        j=JammerDetector()
        r=j.set_baseline(-90)
        self.assertEqual(r["baseline_noise"],-90)
    def test_jamming(self):
        j=JammerDetector()
        j.set_baseline(-90)
        r=j.check_noise_floor(-50)
        self.assertTrue(r["jamming_detected"])
    def test_normal(self):
        j=JammerDetector()
        j.set_baseline(-90)
        r=j.check_noise_floor(-85)
        self.assertFalse(r["jamming_detected"])
    def test_deauth(self):
        j=JammerDetector()
        r=j.analyze_deauth_frames(100,60)
        self.assertTrue(r["attack_detected"])

if __name__=="__main__": unittest.main()
