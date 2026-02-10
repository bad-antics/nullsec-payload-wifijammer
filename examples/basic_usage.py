from nullsec_payload_wifijammer.core import JammerDetector
j=JammerDetector(threshold=10)
j.set_baseline(-90)
for noise in [-85,-60,-40,-95]:
    r=j.check_noise_floor(noise)
    status="JAMMING" if r["jamming_detected"] else "Normal"
    print(f"Noise {noise}dB: {status} (delta: {r['delta']}dB)")
