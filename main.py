import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="MBTI 국가별 분포", layout="wide")

st.title("🌍 MBTI 유형별 비율이 가장 높은 국가 Top 10")

# 국가명 변환 딕셔너리 (필요에 따라 계속 추가 가능)
country_name_map = {
    "United States": "미국",
    "USA": "미국",
    "Korea": "대한민국",
    "South Korea": "대한민국",
    "North Korea": "북한",
    "Japan": "일본",
    "China": "중국",
    "Germany": "독일",
    "France": "프랑스",
    "United Kingdom": "영국",
    "UK": "영국",
    "Canada": "캐나다",
    "Australia": "호주",
    "Brazil": "브라질",
    "India": "인도",
    "Russia": "러시아",
    "Italy": "이탈리아",
    "Spain": "스페인",
    # 필요한 국가를 여기 계속 추가하세요
}

# CSV 업로드
uploaded_file = st.file_uploader("CSV 파일 업로드 (countriesMBTI_16types.csv)", type=["csv"])

if uploaded_file is not None:
    # 데이터 불러오기
    df = pd.read_csv(uploaded_file)

    # 국가 컬럼 및 MBTI 컬럼 분리
    country_col = "Country"
    mbti_cols = [c for c in df.columns if c != country_col]

    # 국가명을 한글로 변환
    df[country_col] = df[country_col].replace(country_name_map)

    # 데이터 long 형태로 변환
    df_long = df.melt(
        id_vars=[country_col],
        value_vars=mbti_cols,
        var_name="MBTI",
        value_name="Value"
    )

    # 값이 숫자가 아닐 경우 처리 (예: 문자열, NaN)
    df_long["Value"] = pd.to_numeric(df_long["Value"], errors="coerce")
    df_long = df_long.dropna(subset=["Value"])

    # MBTI 유형 선택
    mbti_selected = st.selectbox("MBTI 유형을 선택하세요", mbti_cols)

    # 선택된 MBTI에 대해 Top 10 국가
    top10 = (
        df_long[df_long["MBTI"] == mbti_selected]
        .sort_values("Value", ascending=False)
        .head(10)
    )

    st.subheader(f"🌟 {mbti_selected} 유형 비율이 가장 높은 국가 Top 10")

    # Altair 그래프
    chart = (
        alt.Chart(top10)
        .mark_bar()
        .encode(
            x=alt.X("Value:Q", title="비율(%)"),
            y=alt.Y("Country:N", sort="-x", title="국가"),
            tooltip=["Country", "Value"]
        )
        .interactive()
    )

    st.altair_chart(chart, use_container_width=True)

    # 데이터 테이블도 함께 표시
    st.dataframe(top10.reset_index(drop=True))

else:
    st.info("📂 먼저 CSV 파일을 업로드해주세요.")
