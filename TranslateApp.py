import streamlit as st
import whisper

# 翻訳を実行する関数　引数：アップロードされた音声ファイル
def execute_translate(upload_file):
    path = "your path" + upload_file.name
    print("処理開始を受け付けました")
    model = whisper.load_model("small")
    audio = whisper.load_audio(path)
    result = model.transcribe(audio=audio, language="ja", fp16=False)
    st.write(result["text"])
    print("音声書き起こしが終了しました" + "\n")

st.title("自動翻訳システム")
upload_file = st.file_uploader("音声ファイルを選択してください", type=['mp3', 'mp4', 'wav'])

if upload_file is not None:
    st.subheader('ファイル詳細')
    file_details = {'FileName': upload_file.name, 'FileType': upload_file.type, 'FileSize': upload_file.size}
    st.write(file_details)
    file_name=upload_file.name.split('.')[0]
    if st.button("処理開始"):
        with st.spinner('***音声文字起こしを実行中です...***'):
            execute_translate(upload_file)
            
        st.success('***音声文字起こしを完了しました***')