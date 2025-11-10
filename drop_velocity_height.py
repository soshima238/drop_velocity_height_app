import streamlit as st
import math

st.title("液滴落下速度計算ツール（液滴直径＋液膜隙間チェック付き）")

st.markdown("""
液滴中心が指定した高さにあるときの速度を計算します。  
- 下に厚さ **1 mm** の液膜があります。  
- 液滴下端と液膜の間には **少なくとも 0.4 mm の隙間** を確保してください。  
- 入力単位：  
  - H: 落下開始高さ [cm]  
  - z_center: 液滴中心高さ [mm]  
  - D: 液滴直径 [mm]
""")

g = 9.80665  # 重力加速度 [m/s^2]
liquid_film_thickness = 1.0  # mm
min_gap = 0.4  # mm

# 入力欄
H_cm = st.number_input("落下開始高さ H [cm]", min_value=0.5, max_value=1000.0, value=15.0, step=1.0)
z_center_mm = st.number_input("液滴中心高さ z_center [mm]", min_value=1.0, max_va
