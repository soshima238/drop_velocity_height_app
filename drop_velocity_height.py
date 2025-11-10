import streamlit as st
import math

st.title("液滴落下速度計算ツール（液滴直径＋液膜チェック付き）")

st.markdown("""
液滴中心が指定した高さにあるときの速度を計算します。  
- 下に厚さ **1 mm** の液膜があるので、液滴が液膜に接しないように入力してください。  
- 入力単位：  
  - H: 落下開始高さ [cm]  
  - z_center: 液滴中心高さ [mm]  
  - D: 液滴直径 [mm]
""")

g = 9.80665  # 重力加速度 [m/s^2]
liquid_film_thickness = 1.0  # mm

# 入力欄
H_cm = st.number_input("落下開始高さ H [cm]", min_value=0.5, max_value=1000.0, value=15.0, step=1.0)
z_center_mm = st.number_input("液滴中心高さ z_center [mm]", min_value=1.0, max_value=100.0, value=4.0, step=1.0)
D_mm = st.number_input("液滴直径 D [mm]", min_value=0.1, max_value=100.0, value=4.0, step=0.1)

# 単位変換
H = H_cm / 100.0              # cm → m
z_center = z_center_mm / 1000.0  # mm → m
D = D_mm / 1000.0              # mm → m
film_top = liquid_film_thickness / 1000.0  # mm → m

# チェック
if z_center - D/2 <= film_top:
    st.warning(f"液滴下端が液膜厚 {liquid_film_thickness} mm を超えるように液滴中心高さと直径を調整してください。")
elif H <= z_center:
    st.warning("落下開始高さ H は液滴中心より高い値にしてください。")
else:
    v = math.sqrt(2 * g * (H - z_center))
    st.success(f"液滴中心が {z_center_mm:.1f} mm の高さにあるときの速度: **{v:.3f} m/s**")

st.caption("※空気抵抗は無視しています。")
