### Project Description

The **Smart Drain Monitoring System** is an IoT and machine learning based solution designed to detect early signs of drain blockage and prevent urban flooding. In many cities, drainage systems get clogged due to plastic waste, debris, and rising water levels. These issues are usually detected only after the drain is already blocked, leading to water overflow and sanitation problems.

This project uses a **NodeMCU (ESP8266)** microcontroller connected to sensors such as a **water level sensor** and an **ultrasonic sensor** to continuously monitor conditions inside a drain. The sensors collect real-time data such as the level of water in the drain and the distance to accumulated waste.

The collected sensor data is transmitted to a monitoring interface where a **machine learning model analyzes the readings** to identify patterns that indicate possible blockage. Based on this analysis, the system classifies the drain condition (for example, normal, warning, or blocked) and generates alerts when abnormal conditions are detected.

By providing **early warnings before a complete blockage occurs**, the system helps municipal authorities take preventive action and reduce the risk of flooding. The design focuses on being **low-cost, scalable, and suitable for smart city infrastructure**.

### Features
1. Real-Time Drain Monitoring

The system continuously collects data from sensors placed inside the drain to monitor environmental conditions.

Examples:

* The water level sensor measures the height of water inside the drain.
* The ultrasonic sensor measures the distance between the sensor and waste accumulation.

2. Waste Accumulation Detection

The ultrasonic sensor detects the buildup of waste by measuring changes in distance.

Examples:

* When plastic waste accumulates, the distance measured by the ultrasonic sensor decreases.
* When the drain is clean, the measured distance remains larger and stable.

3. Machine Learning-Based Prediction

A trained machine learning model analyzes sensor data to determine the condition of the drain.

Examples:

* Normal water level and stable distance → system classifies the drain as **Normal**.
* Rapid water level rise with decreasing distance → system predicts **Possible Blockage**.

4. Early Warning Alerts

The system can generate alerts when abnormal patterns indicate a risk of blockage.

Examples:

* If water level rises quickly during rainfall, the system triggers a warning.
* If waste accumulation reaches a critical level, the system sends a blockage alert.

5. Low-Cost IoT Implementation

The project uses inexpensive and widely available hardware components.

Examples:

* NodeMCU (ESP8266) for sensor control and communication.
* Standard sensors like water level and ultrasonic modules.

6. Scalable Smart City Solution

Multiple monitoring units can be installed across different drains in a city.

Examples:

* Each drain can have one monitoring unit collecting data.
* Data from multiple drains can be combined in a central monitoring dashboard.
