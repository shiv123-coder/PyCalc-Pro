# PyCalc Pro Chrome Extension

This folder contains the official Google Chrome Extension for PyCalc Pro. It allows you to access the intelligent calculator dashboard instantly from your browser toolbar!

## How to Install the Extension

Since this extension is loaded locally (unpacked), please follow these simple steps to install it in Google Chrome or any Chromium-based browser (Edge, Brave, Arc):

1. **Open the Extensions Page**: 
   Open your browser and navigate to `chrome://extensions/` in the URL bar.

2. **Enable Developer Mode**:
   In the top-right corner of the Extensions page, toggle the switch that says **"Developer mode"** to the ON position.

3. **Load the Extension**:
   - Click the **"Load unpacked"** button that appears in the top-left corner.
   - A file dialog will open. Navigate to the PyCalc-Pro project folder on your computer.
   - Select the `chrome_extension` folder and click **Select Folder**.

4. **Pin the Extension (Optional but recommended)**:
   - Click the puzzle piece icon 🧩 in your browser toolbar (top right).
   - Find "PyCalc Pro Extension" in the list.
   - Click the **Pin icon** 📌 next to it to keep it visible on your toolbar for instant access.

## How it Works

The extension uses an `iframe` to load your live Streamlit Community Cloud application (`https://pycalc-pro-shiv.streamlit.app/`). The URL includes the `/?embed=true` parameter, which hides the Streamlit sidebar, header, and footer, providing a clean, app-like experience within the extension popup.

You will have full access to the Smart Expression Bar, Sudoku Solver, Matrix Operations, and all other PyCalc Pro features without ever leaving your current web page!
