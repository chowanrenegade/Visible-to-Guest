OVERVIEW This script automates the process of updating the "Visible to Guest" status for items in your inventory. It reads from a source file and applies visibility rules based on the "Sub-category" of each item.

NOTE: Only works in IDLE

FILE REQUIREMENTS

Input File: Must be named "parts.csv"

Location: The CSV file must be in the same folder as the script.

Columns: The CSV must contain columns named "Sub-category" and "Visible to Guest".

HOW TO USE

Ensure your data file is named "parts.csv" and is in the script folder.

Run the script using IDLE.

The script will check for the file and process the updates.

A new file named "updated_parts_list.csv" will be generated. Note: The original "parts.csv" file will remain unchanged.

LOGIC RULES The following items will be updated automatically:

Set to 'Y' (Visible):

Electronics

Fans

Appearance And Maintenance

Venting

Set to 'N' (Hidden):

Burner Parts

Conversion Kits

Orifices

Pilot Assemblies

Thermocouple And Thermopiles

Valves

Any Sub-category not listed above will keep its original value.
