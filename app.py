import streamlit as st
import pandas as pd
import numpy as np
import requests
import zipfile
import io
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Config ---
st.set_page_config(page_title="AI Maintenance Dashboard", layout="wide")

# --- Header ---
st.title("🏭 AI-Powered Predictive Maintenance Dashboard")
st.markdown("""
**Team Exceptional (Group 1)** | ITAI 2277 Capstone (Fall 2025)  
*Real-time monitoring of industrial turbofan engines using AI.*
""")

# --- 1. Robust Data Loading Function ---
@st.cache_data
def load_data():
    filename = 'train_FD001.txt'
    if not os.path.exists(filename):
        try:
            with st.spinner('Downloading NASA CMAPSS Data...'):
                url = "https://data.nasa.gov/docs/legacy/CMAPSSData.zip"
                response = requests.get(url, timeout=15)
                response.raise_for_status()
                with zipfile.ZipFile(io.BytesIO(response.content)) as z:
                    z.extractall()
            st.success("Data downloaded successfully!")
        except Exception as e:
            st.warning(f"⚠️ Download failed ({str(e)}). Switching to DEMO MODE with synthetic data.")
            return generate_synthetic_data()

    try:
        col_names = ['unit', 'cycle', 'op1', 'op2', 'op3'] + [f'sensor{i}' for i in range(1, 22)]
        df = pd.read_csv(filename, sep=' ', header=None, names=col_names, index_col=False)
        df = df.dropna(axis=1)
        # Feature Engineering
        df['rul'] = df.groupby('unit')['cycle'].transform(lambda x: x.max() - x)
        df['failure_label'] = (df['rul'] <= 30).astype(int)
        return df
    except Exception:
        return generate_synthetic_data()

def generate_synthetic_data():
    st.info("ℹ️ Running in DEMO MODE with synthetic data.")
    units = []
    for u in range(1, 11):
        cycles = np.arange(1, 150)
        df_u = pd.DataFrame({'unit': u, 'cycle': cycles})
        df_u['sensor11'] = 20 + (cycles * 0.05) + np.random.normal(0, 0.5, len(cycles))
        df_u['sensor4'] = 1400 + (cycles * 0.1) + np.random.normal(0, 2, len(cycles))
        for i in [2,3,7,8,12,13,15,17,20,21]:
            df_u[f'sensor{i}'] = np.random.rand(len(cycles))
        df_u['rul'] = 150 - cycles
        df_u['failure_label'] = (df_u['rul'] <= 30).astype(int)
        units.append(df_u)
    return pd.concat(units)

# --- 2. Training Function ---
@st.cache_resource
def train_model(df):
    features = ['sensor2', 'sensor3', 'sensor4', 'sensor7', 'sensor8', 'sensor11', 
                'sensor12', 'sensor13', 'sensor15', 'sensor17', 'sensor20', 'sensor21']
    available_features = [f for f in features if f in df.columns]

    X = df[available_features]
    y = df['failure_label']

    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestClassifier(n_estimators=10, max_depth=5, random_state=42)
    model.fit(X_scaled, y)
    return model, scaler, available_features

# --- 3. Dashboard Logic ---
try:
    df = load_data()
    model, scaler, feature_cols = train_model(df)

    st.sidebar.header("Control Panel")
    selected_unit = st.sidebar.selectbox("Select Engine Unit ID", df['unit'].unique())
    unit_data = df[df['unit'] == selected_unit]
    max_cycle = int(unit_data['cycle'].max())
    current_cycle = st.sidebar.slider("Current Operational Cycle", 1, max_cycle, max_cycle)

    current_row = unit_data[unit_data['cycle'] == current_cycle]

    if not current_row.empty:
        input_data = current_row[feature_cols]
        input_scaled = scaler.transform(input_data)
        fail_prob = model.predict_proba(input_scaled)[0][1]
        true_rul = current_row['rul'].values[0]

        col1, col2, col3 = st.columns(3)
        col1.metric("Current Cycle", f"{current_cycle}")
        col2.metric("True RUL", f"{true_rul}")
        color = "inverse" if fail_prob > 0.5 else "normal"
        col3.metric("Failure Probability", f"{fail_prob:.1%}", delta_color=color)

        if fail_prob > 0.5:
            st.error(f"⚠️ ALERT: High Failure Risk Detected for Engine {selected_unit}!")
        else:
            st.success(f"✅ Engine {selected_unit} Operating Normally.")

        st.subheader("Sensor Degradation Analysis")
        fig, ax = plt.subplots(figsize=(10, 3))
        sns.lineplot(data=unit_data, x='cycle', y='sensor11', label='Sensor 11 (Pressure)', ax=ax)
        plt.axvline(x=current_cycle, color='red', linestyle='--', label='Current Time')
        st.pyplot(fig)
except Exception as e:
    st.error(f"Application Error: {e}")
