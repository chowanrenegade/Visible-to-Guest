# Inventory Visibility Automator

This script automates the process of updating the **"Visible to Guest"** status for inventory items. It reads from a source file and applies visibility rules based on the **"Sub-category"** of each item.

> **Note:** This script is designed to run in **IDLE**.

---

## 🛠 File Requirements

* **Filename:** Must be named `parts.csv`.
* **Location:** The CSV file must be in the same folder as the script.
* **Columns:** The CSV must contain columns named `Sub-category` and `Visible to Guest`.

---

## 🚀 How To Use

1.  Ensure your data file is named `parts.csv` and is in the script folder.
2.  Run the script using **IDLE**.
3.  The script will check for the file and process the updates.
4.  A new file named `updated_parts_list.csv` will be generated. 

*Note: The original `parts.csv` file will remain unchanged.*

---

## ⚖️ Logic Rules

The script automatically applies the following updates based on the **Sub-category**:

### **Set to 'Y' (Visible)**
* Electronics
* Fans
* Appearance And Maintenance
* Venting

### **Set to 'N' (Hidden)**
* Burner Parts
* Conversion Kits
* Orifices
* Pilot Assemblies
* Thermocouple And Thermopiles
* Valves

> [!TIP]
> Any Sub-category not listed above will keep its original value.
