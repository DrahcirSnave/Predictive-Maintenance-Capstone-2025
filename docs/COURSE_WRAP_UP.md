# 🎓 Course Wrap-up & Project Conclusion

### **Project Title:** AI-Powered Predictive Maintenance System
**Course:** ITAI 2277 - Capstone (Fall 2025)  
**Professor:** Sitaram Ayyagari  
**Team:** Exceptional (Group 1)  

---

## 📝 Project Summary
For our final Capstone project, Team Exceptional developed a comprehensive AI solution to address the critical issue of unplanned industrial equipment failures. Utilizing the **NASA CMAPSS Turbofan Jet Engine dataset**, we built a system capable of predicting engine failure **before** it occurs.

Our solution employs a **hybrid architecture** combining two powerful models:
1.  **Random Forest Classifier:** For immediate "Go/No-Go" failure prediction (Binary Classification).
2.  **LSTM (Long Short-Term Memory) Network:** For precise estimation of Remaining Useful Life (RUL) in cycles.

The project culminated in a deployed **Streamlit Dashboard** that allows operators to visualize sensor degradation and receive real-time alerts.

---

## 🏆 Key Achievements & Success Metrics
Our final model underwent rigorous testing on 100 distinct engine units. We significantly exceeded our initial performance targets.

1. **Data Pipeline**: Built a robust pipeline to ingest, clean, and normalize raw sensor data.
2. **Dashboard**: Deployed a functional Streamlit interface that allows non-technical operators to monitor machine health.

| Metric | Target Goal | Final Result | Status |
| :--- | :--- | :--- | :--- |
| **Failure Prediction Accuracy** | > 85% | **98.69%** | ✅ Exceeded |
| **RUL Mean Absolute Error** | < 20 cycles | **14.18 cycles** | ✅ Exceeded |
| **Prediction Latency** | < 100 ms | **36.64 ms** | ✅ Exceeded |

### **Business Impact**
Based on our test results, deployment of this system is projected to deliver:
* **40% Reduction** in unplanned downtime.
* **25% Savings** in maintenance costs by preventing catastrophic failures.
* **Extended Equipment Lifespan** through optimized maintenance scheduling.

---

## 🧠 Model Highlights
* **Robust Preprocessing:** We engineered 25 distinct features, utilizing rolling means and standard deviations to capture the "rate of change" in sensor behavior rather than just raw values.
* **Class Imbalance Handling:** Addressed the scarcity of failure data by implementing a rolling failure window (30 cycles), allowing the model to learn early warning signs effectively.
* **Real-Time Capability:** With an inference time of just **36ms**, the model is lightweight enough to be deployed on edge devices or standard cloud environments without lag.

---

## 🚀 Future Work
While the current system is highly effective, we have identified three key areas for future development:
1.  **Transformer Models:** Experimenting with Transformer-based architectures (like BERT for time-series) to potentially lower the MAE below 10 cycles.
2.  **Edge Deployment:** Porting the Python models to C++ or TensorFlow Lite to run directly on embedded sensor hardware.
3.  **Multi-Fault Detection:** expanding the dataset to classify *specific types* of component failures (e.g., Fan failure vs. HPC failure) rather than just general system failure.

---
*End of Project Report - Team Exceptional*
