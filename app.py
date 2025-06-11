import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title(" 自己分析アプリ")

# 入力欄
user_text = st.text_area("学生時代に頑張ったことを書いてください")

# 評価視点の選択（強み分析のみ）
category = st.selectbox("評価したい視点を選んでください", ["強み分析"])

# キーワードリスト（カテゴリごと）
leadership_keywords = ["リーダー", "まとめた", "指摘をした", "指導", "率いた"]
continuity_keywords = ["コツコツ", "継続", "毎日", "根気", "努力"]
problem_solving_keywords = ["工夫", "改善", "問題解決", "対処", "分析"]
teamwork_keywords = ["協力", "仲間", "チーム", "連携", "サポート"]
initiative_keywords = ["自発的", "自ら", "率先", "主体性", "挑戦"]

# 分析実行
if st.button("分析スタート！") and user_text:
    with st.spinner("分析中..."):
        # スコア初期化
        scores = {
            "リーダーシップ": 0,
            "継続力": 0,
            "課題解決力": 0,
            "チームワーク": 0,
            "主体性": 0
        }

        # キーワード判定（含まれていたら加点）
        if any(kw in user_text for kw in leadership_keywords):
            scores["リーダーシップ"] += 4
        if any(kw in user_text for kw in continuity_keywords):
            scores["継続力"] += 4
        if any(kw in user_text for kw in problem_solving_keywords):
            scores["課題解決力"] += 4
        if any(kw in user_text for kw in teamwork_keywords):
            scores["チームワーク"] += 4
        if any(kw in user_text for kw in initiative_keywords):
            scores["主体性"] += 4

        # 結果表示（強み分析のみ）
        total_score = sum(scores.values())
        if total_score == 0:
            st.write("入力された内容から明確な強みを特定できませんでした。もう少し具体的に書いてみてください。")
        else:
            top_strength = max(scores, key=scores.get)
            st.success("✅ 分析結果")
            st.write(f"あなたの強みは **{top_strength}** です。")

            # レーダーチャート作成
            labels = list(scores.keys())
            values = list(scores.values())
            values += values[:1]  # 閉じるため最初の値を最後に追加

            angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
            angles += angles[:1]

            fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
            ax.set_theta_offset(np.pi / 2)
            ax.set_theta_direction(-1)

            ax.set_thetagrids(np.degrees(angles[:-1]), labels)

            ax.plot(angles, values, color='red', linewidth=2)
            ax.fill(angles, values, color='red', alpha=0.25)

            ax.set_ylim(0, 5)
            ax.set_title("強みのレーダーチャート")

            st.pyplot(fig)
