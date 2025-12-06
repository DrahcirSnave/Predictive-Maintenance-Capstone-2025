# Predictive-Maintenance-Capstone-2025
Team_1_Exceptional

# AI-Powered Predictive Maintenance System 🏭

### 🏆 Capstone Project | Team Exceptional (Group 1)
**Course:** ITAI 2277 (Fall 2025)  
**Professor:** Sitaram Ayyagari  
**Authors:** Miguel Mora, Richard Evans, Akinbobola Akinpelu, Jade Sanchez, Olugbenga Adegoroye

---

## 📖 Project Showcase
Unplanned equipment failures cost industrial businesses billions in downtime and repairs. Our solution uses Artificial Intelligence to predict when machines will fail *before* it happens.

**The Goal:**
To build a Predictive Maintenance System that analyzes sensor data from turbofan engines to forecast **Remaining Useful Life (RUL)** and provide early warnings for failures.

### 🛠️ Solution Architecture
We utilize a dual-model approach to ensure reliability and precision:
1.  **Random Forest Classifier**: Predicts binary failure (Will it fail in the next 30 cycles?).
2.  **LSTM Neural Network**: Predicts exact Remaining Useful Life (RUL) in cycles.

```mermaid
graph LR
    A[Sensor Data Input] --> B[Data Preprocessing];
    B --> C{AI Model};
    C -->|Random Forest| D[Failure Probability];
    C -->|LSTM| E[RUL Prediction];
    D --> F[Streamlit Dashboard];
    E --> F;
    F --> G[Maintenance Alert];
```
---
### 📊 Key Results (Achieved)
* **Failure Prediction Accuracy:** 98.69% ✅
* **RUL Mean Absolute Error:** 14.18 cycles ✅
* **Prediction Latency:** 36.64 ms (Real-time capable) ✅

* **Latency:** < 100ms (Real-time capable)
* **Business Impact:** Estimated 40% reduction in downtime and 25% cost savings.
---

## 🎥 Formal Project Presentation
You can view our full project presentation slides here:
[**View Final Presentation Slides**](./Team%201_CapStoneFinal_FinalPresentation_ITAI2277.pptx)

*(Note: Please download the file to view the full PowerPoint)*

---
  
