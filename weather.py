import sys
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # Widgets
        self.city_label = QLabel("Enter City name: ")
        self.city_input = QLineEdit()
        self.get_weather_button = QPushButton("Get Weather")
        self.temperature_label = QLabel("Temperature: --°C")
        self.emoji_label = QLabel("☀️")
        self.description_label = QLabel("Condition: ---")

        # Setting up UI
        self.initUI()

        # Fetching weather
        self.get_weather_button.clicked.connect(self.get_weather)

        self.city_input.returnPressed.connect(self.get_weather)


    def initUI(self):
        self.setWindowTitle("Weather App")

        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.get_weather_button)
        layout.addWidget(self.temperature_label)
        layout.addWidget(self.emoji_label)
        layout.addWidget(self.description_label)

        self.setLayout(layout)

    def get_weather(self):
        city = self.city_input.text()
        if not city:
            self.description_label.setText("⚠️ Please enter a city!")
            return

        api_key = "3fbe4efc06ef15e7e2b0b23b83cb8bee"  #API KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != 200:
                self.description_label.setText("❌ City not found")
                return

            # For Weather info
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]

            # Choosing emoji acc to weather
            weather_main = data["weather"][0]["main"].lower()
            if "cloud" in weather_main:
                emoji = "☁️"
            elif "rain" in weather_main:
                emoji = "🌧️"
            elif "clear" in weather_main:
                emoji = "☀️"
            elif "snow" in weather_main:
                emoji = "❄️"
            else:
                emoji = "🌍"

            # Update labels
            self.temperature_label.setText(f"Temperature: {temp}°C")
            self.description_label.setText(f"Condition: {description.capitalize()}")
            self.emoji_label.setText(emoji)

        except Exception as e:
            self.description_label.setText("⚠️ Error fetching data")
            print("Error:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
=======
import sys
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout
)


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # Widgets
        self.city_label = QLabel("Enter City name: ")
        self.city_input = QLineEdit()
        self.get_weather_button = QPushButton("Get Weather")
        self.temperature_label = QLabel("Temperature: --°C")
        self.emoji_label = QLabel("☀️")
        self.description_label = QLabel("Condition: ---")

        # Setting up UI
        self.initUI()

        # Fetching weather
        self.get_weather_button.clicked.connect(self.get_weather)

        self.city_input.returnPressed.connect(self.get_weather)


    def initUI(self):
        self.setWindowTitle("Weather App")

        layout = QVBoxLayout()
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.get_weather_button)
        layout.addWidget(self.temperature_label)
        layout.addWidget(self.emoji_label)
        layout.addWidget(self.description_label)

        self.setLayout(layout)

    def get_weather(self):
        city = self.city_input.text()
        if not city:
            self.description_label.setText("⚠️ Please enter a city!")
            return

        api_key = "3fbe4efc06ef15e7e2b0b23b83cb8bee"  #API KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != 200:
                self.description_label.setText("❌ City not found")
                return

            # For Weather info
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]

            # Choosing emoji acc to weather
            weather_main = data["weather"][0]["main"].lower()
            if "cloud" in weather_main:
                emoji = "☁️"
            elif "rain" in weather_main:
                emoji = "🌧️"
            elif "clear" in weather_main:
                emoji = "☀️"
            elif "snow" in weather_main:
                emoji = "❄️"
            else:
                emoji = "🌍"

            # Update labels
            self.temperature_label.setText(f"Temperature: {temp}°C")
            self.description_label.setText(f"Condition: {description.capitalize()}")
            self.emoji_label.setText(emoji)

        except Exception as e:
            self.description_label.setText("⚠️ Error fetching data")
            print("Error:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

