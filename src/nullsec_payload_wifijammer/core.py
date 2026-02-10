"""WiFi Jammer Detection"""
import time,json,subprocess,re

class JammerDetector:
    def __init__(self,threshold=10):
        self.threshold=threshold
        self.baseline_noise=None
    
    def set_baseline(self,noise_floor=-90):
        self.baseline_noise=noise_floor
        return {"baseline_noise":noise_floor,"status":"calibrated"}
    
    def check_noise_floor(self,current_noise):
        if self.baseline_noise is None: self.set_baseline()
        delta=current_noise-self.baseline_noise
        return {"current":current_noise,"baseline":self.baseline_noise,"delta":delta,
                "jamming_detected":delta>20,"severity":"HIGH" if delta>30 else "MEDIUM" if delta>20 else "LOW"}
    
    def analyze_deauth_frames(self,frame_count,time_window=60):
        rate=frame_count/max(time_window,1)
        return {"deauth_count":frame_count,"time_window":time_window,"rate_per_sec":round(rate,2),
                "attack_detected":rate>self.threshold/60,"severity":"CRITICAL" if rate>1 else "HIGH" if rate>0.5 else "MEDIUM"}
    
    def get_channel_quality(self,interface="wlan1mon"):
        try:
            result=subprocess.check_output(["iwconfig",interface],text=True)
            quality=re.search(r"Link Quality[=:](\d+)/(\d+)",result)
            if quality: return {"quality":int(quality.group(1)),"max":int(quality.group(2))}
        except: pass
        return {"quality":"unknown"}
