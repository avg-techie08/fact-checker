import os
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont

def generate_samples():
    os.makedirs("static/samples", exist_ok=True)
    
    # 1. Generate Hindi Voice Note (sample_scooter.mp3)
    hindi_text = (
        "नमस्कार! केंद्र सरकार की नई योजना के तहत सभी भारतीय युवाओं और महिलाओं को "
        "मुफ्त इलेक्ट्रिक स्कूटर दिया जा रहा है। अपना आधार कार्ड नंबर भेजकर तुरंत "
        "फ्री इलेक्ट्रिक स्कूटी योजना में रजिस्ट्रेशन करें।"
    )
    print("Generating Hindi voice sample...")
    tts = gTTS(text=hindi_text, lang='hi', slow=False)
    tts.save("static/samples/sample_scooter.mp3")
    print("Saved static/samples/sample_scooter.mp3")
    
    # 2. Generate Fake Notice Screenshot (sample_blackout.png)
    print("Generating fake electricity blackout notice image...")
    width, height = 700, 480
    image = Image.new("RGB", (width, height), color="#f8fafc")
    draw = ImageDraw.Draw(image)
    
    # Border & Header banner
    draw.rectangle([(20, 20), (width - 20, height - 20)], fill="#ffffff", outline="#dc2626", width=3)
    draw.rectangle([(20, 20), (width - 20, 90)], fill="#dc2626")
    
    # Text helper
    try:
        font_header = ImageFont.truetype("arial.ttf", 26)
        font_sub = ImageFont.truetype("arial.ttf", 16)
        font_body = ImageFont.truetype("arial.ttf", 15)
        font_bold = ImageFont.truetype("arialbd.ttf", 16)
        font_footer = ImageFont.truetype("arial.ttf", 13)
    except Exception:
        font_header = ImageFont.load_default()
        font_sub = font_header
        font_body = font_header
        font_bold = font_header
        font_footer = font_header

    draw.text((width // 2, 45), "URGENT OFFICIAL CIRCULAR", fill="#ffffff", font=font_header, anchor="mm")
    draw.text((width // 2, 72), "STATE ELECTRICITY REGULATORY & TRANSMISSION BOARD", fill="#fef2f2", font=font_sub, anchor="mm")
    
    # Watermark / Fake Reference
    draw.text((40, 110), "Ref No: DISCOM/EMG-GRID/2026/091", fill="#64748b", font=font_footer)
    draw.text((width - 40, 110), "Date: Immediate Broadcast", fill="#64748b", font=font_footer, anchor="ra")
    draw.line([(40, 130), (width - 40, 130)], fill="#e2e8f0", width=2)
    
    # Notice content
    draw.text((40, 145), "SUBJECT: COMPLETE POWER GRID SHUTDOWN TONIGHT (10 PM - 6 AM)", fill="#991b1b", font=font_bold)
    
    body_lines = [
        "This is to formally notify all domestic and commercial consumers that the Northern",
        "National Power Grid is operating under critical load distress.",
        "",
        "Consequently, power supply will remain completely suspended tonight across all zones.",
        "ALL INVERTERS AND BATTERY STORAGE UNITS MUST BE POWERED OFF IMMEDIATELY.",
        "Failure to disconnect backup inverters may cause permanent transformer burnout",
        "and will attract a mandatory fine of Rs. 10,000 under the Electricity Act.",
        "",
        "Kindly forward this alert to all residential WhatsApp groups immediately."
    ]
    
    y = 180
    for line in body_lines:
        if "MUST BE POWERED OFF" in line or "mandatory fine" in line:
            draw.text((40, y), line, fill="#b91c1c", font=font_bold)
        else:
            draw.text((40, y), line, fill="#1e293b", font=font_body)
        y += 24
        
    # Fake Seal & Sign
    draw.rectangle([(width - 240, height - 100), (width - 40, height - 40)], outline="#94a3b8", width=1, fill="#f1f5f9")
    draw.text((width - 140, height - 80), "CHIEF POWER CONTROLLER", fill="#0f172a", font=font_bold, anchor="mm")
    draw.text((width - 140, height - 60), "[VERIFIED OFFICIAL ORDER]", fill="#059669", font=font_footer, anchor="mm")
    
    image.save("static/samples/sample_blackout.png")
    print("Saved static/samples/sample_blackout.png")

if __name__ == "__main__":
    generate_samples()
