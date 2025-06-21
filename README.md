# DC Microgrid Fault Detection using Support Vector Classification

This project focuses on detecting and classifying faults in a **DC microgrid system** using **Support Vector Classification (SVC)**, a machine learning technique known for its robustness in binary and multi-class classification problems. The model is trained to distinguish between **pole-to-pole** and **pole-to-ground** faults, enabling early fault diagnosis and improving the reliability of DC power systems.

---

## Features

* Accurate classification of DC microgrid faults using machine learning
* Support Vector Classification (SVC) model trained on labeled fault data
* Dataset contains binary labels:
  `+1` → Pole-to-Pole Fault
  `-1` → Pole-to-Ground Fault
* High accuracy (\~96%) achieved using polynomial kernel
* Ideal for power system monitoring, smart grids, and renewable integration

---

## Tech Stack

* Python 3.x
* scikit-learn
* pandas
* NumPy
* Matplotlib (for visualization)

---

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/Anirban-2005/dc-microgrid-fault-detection.git
   cd dc-microgrid-fault-detection
   ```
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:

   ```bash
   python dc_fault_detection.py
   ```
4. Review the console and visual outputs for model performance and classification results.

---

## Dataset Overview

* The dataset is preprocessed and labeled.
* Features include voltage, current, and other electrical parameters.
* Target classes:

  * `+1`: Pole-to-Pole Fault
  * `-1`: Pole-to-Ground Fault

---

## Who is this for?

This project is aimed at:

* Electrical and power systems engineers
* Machine learning researchers
* Smart grid developers
* Students and educators in electrical engineering and data science

---

## Future Improvements

* Integration with real-time sensor data via IoT
* Fault classification in hybrid AC/DC microgrids
* Real-time deployment using Raspberry Pi or edge devices

---

## Contact

For any suggestions or queries, feel free to open an issue or reach out via GitHub.

---

>  "Reliable power begins with intelligent fault detection."
