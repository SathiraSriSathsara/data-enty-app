# Product Entry CSV Application

A user-friendly Python application designed for data entry operators to quickly input product information and save it into a CSV file. This software simplifies the process of entering product data by auto-generating IDs and providing a modern GUI with seamless navigation.

## Features

- **Auto-generated ID**: Automatically generates a unique ID for each product based on the previous entry.
- **Input Fields**: Includes fields for barcode, name, price, stock, category, and unit of measurement.
- **Enter Key Navigation**: Automatically navigates to the next input box when the Enter key is pressed, enhancing the user experience.
- **CSV Saving**: Saves product data into a CSV file with a single press of the Enter key on the last input field.
- **Success Message**: Displays a success message at the top of the application with the generated ID upon saving.
- **Splash Screen**: Features a splash screen that fades in and out, adding a professional touch to the application.
- **Clear Button**: Resets all input fields for new entries.
- **Modern Design**: A clean and modern interface without unnecessary borders and controls.

## Requirements

- Python 3.x
- Tkinter (included with standard Python installations)
- PyInstaller (for compiling the application into an executable)

## Installation

1. Clone the repository:

   ```bash
   git clone hhttps://github.com/SathiraSriSathsara/data-enty-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd data-enty-app
   ```

3. Install the required dependencies (if any):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python data.py
   ```

2. Enter the product details into the fields provided.
3. Press Enter to navigate through the input fields. When you reach the "Unit of Measurement" field, pressing Enter will save the product data to the CSV file and display a success message at the top.
4. To clear the fields for a new entry, click the **Clear** button.

## Compiling to Executable

To compile the application into a standalone executable:

1. Install PyInstaller (if you haven't already):

   ```bash
   pip install pyinstaller
   ```

2. Navigate to the project directory:

   ```bash
   cd product-entry-csv-app
   ```

3. Run the following command:

   ```bash
   pyinstaller --onefile --windowed data.py
   ```

4. Find the generated `.exe` file in the `dist` folder.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source community for providing the libraries and resources that made this project possible.
```

