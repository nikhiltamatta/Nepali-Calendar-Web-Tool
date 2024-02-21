# Nepali Calendar Web Tool

Welcome to the Nepali Calendar Web Tool! This tool provides a simple web interface to convert dates from the Bikram Sambat (BS) calendar to the Gregorian calendar (AD) using Python.

📅🌞

## Setup

To set up and use the Nepali Calendar Web Tool, follow these steps:

1. **Clone the Repository**: 
   ```
   git clone https://github.com/nikhiltamatta/nepali-calendar-web-tool.git
   ```

2. **Install Dependencies**: 
   ```
   pip install Flask nepali-calendar
   ```

3. **Run the Flask Application**: 
   ```
   python nepali_calendar_app.py
   ```

4. **Make POST Requests**:
   You can make POST requests to `http://localhost:5000/convert_bs_to_ad` with JSON data containing the BS year, month, and day to get the corresponding AD date.

## Usage

Once the Flask application is running, you can use the Nepali Calendar Web Tool as follows:

1. Send a POST request to `http://localhost:5000/convert_bs_to_ad` with JSON data containing the BS year, month, and day.
   Example POST request body:
   ```json
   {
     "bs_year": 2078,
     "bs_month": 11,
     "bs_day": 10
   }
   ```

2. You will receive a JSON response with the corresponding AD date.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

🎉🚀

## License

This project is licensed under the [MIT License](LICENSE).
