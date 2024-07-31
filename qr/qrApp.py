from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.clock import Clock
import cv2
import webbrowser

class QrcodeDetector(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Yellow'
        
        layout = MDBoxLayout(orientation='vertical')
        
        self.image = Image()
        layout.add_widget(self.image)
        
        self.detect_url_button = MDFillRoundFlatButton(
            text="Detect URL",
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            size_hint=(None, None)
        )
        self.detect_url_button.bind(on_press=self.open_detected_url)
        layout.add_widget(self.detect_url_button)
        
        self.capture = cv2.VideoCapture(0)
        self.detector = cv2.QRCodeDetector()
        self.url_opened = False
        
        Clock.schedule_interval(self.load_video, 1.0 / 30.0)
        
        return layout

    def load_video(self, *args):
        ret, frame = self.capture.read()
        
        if ret:
            data, bbox, _ = self.detector.detectAndDecode(frame)
            self.data = data.strip()  # Ensure no leading/trailing spaces
            
            if data and not self.url_opened:
                print(f"Detected QR Code data: {data}")
                
            if bbox is not None:
                buffer = cv2.flip(frame, 0).tobytes()
                texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
                texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
                self.image.texture = texture

    def open_detected_url(self, *args):
        if self.data:
            if not self.data.startswith("http"):
                self.data = "http://" + self.data  # Ensure it is a valid URL format
            
            print(f"Opening URL: {self.data}")
            webbrowser.open(self.data)
            self.url_opened = True
        else:
            print("No URL detected")

if __name__ == '__main__':
    QrcodeDetector().run()
