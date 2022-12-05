import streamlit as st
#タイトル
st.title('感覚的なツイートをしよう！！')

#性別
color = st.select_slider(
    'Select あなたの性別を教えてください',
    options=['女性', '女性？', '女性？？', '中性', '男性？？', '男性？', '男性'])

#感情選択
genre = st.radio(
    "あなたの今の気持ちを教えて？",
    ('楽しい', '悲しい', 'うれしい','怒っている','何も感じない'))


#カラーピッカー
color = st.color_picker('色を選んでください', '#00f900')
st.write('あなたの色は', color)
    
#白の語彙
if color == '#ffffff' and genre == '楽しい' :
  st.header('おすすめ検索ワード:rabbit')
    
    
if color == '#ffffff' and genre == '悲しい' :
    st.header('おすすめ検索ワード:snow')
       
if color == '#ffffff' and genre == 'うれしい' :
        st.header('おすすめ検索ワード:excite')
        
if color == '#ffffff' and genre == '怒っている' :
           st.header('おすすめ検索ワード:bomb')
            
if color == '#ffffff' and genre == '何も感じない' :
               st.header('おすすめ検索ワード:nothingness')
                
#黒の語彙
if color == '#000000' and genre == '楽しい' :
    st.header('おすすめ検索ワード:Sunburn')
    
    
if color == '#000000' and genre == '悲しい' :
    st.header('おすすめ検索ワード:darkness')
       
if color == '#000000' and genre == 'うれしい' :
      st.header('おすすめ検索ワード:candle')
        
if color == '#000000' and genre == '怒っている' :
            st.header('おすすめ検索ワード:devil')
            
if color == '#000000' and genre == '何も感じない' :
                st.header('おすすめ検索ワード:Cruelty')   
                
#赤の語彙
if color == '#ff0000' and genre == '楽しい' :
                    st.header('おすすめ検索ワード:Sun')
                    
                    
if color == '#ff0000' and genre == '悲しい' :
                    st.write('おすすめ検索ワード:blood')
                       
if color == '#ff0000' and genre == 'うれしい' :
                        st.header('おすすめ検索ワード:apple')
                        
if color == '#ff0000' and genre == '怒っている' :
                            st.header('おすすめ検索ワード:fire')
                            
if color == '#ff0000' and genre == '何も感じない' :
                            st.header('おすすめ検索ワード:prominence') 
#緑の語彙
if color == '#00f900' and genre == '楽しい' :
                   st.header('おすすめ検索ワード:forest')
                    
                    
if color == '#00f900' and genre == '悲しい' :
                   st.header('おすすめ検索ワード:death')
                       
if color == '#00f900' and genre == 'うれしい' :
                       st.header('おすすめ検索ワード:slime')
                        
if color == '#00f900' and genre == '怒っている' :
                          st.header('おすすめ検索ワード:god')
                            
if color == '#00f900' and genre == '何も感じない' :
                           st.header('おすすめ検索ワード:goddess')
#青の語彙
if color == '#2300F9' and genre == '楽しい' :
                    st.header('おすすめ検索ワード:sky')
                    
                    
if color == '#2300F9' and genre == '悲しい' :
                    st.header('おすすめ検索ワード:sea')
                       
if color == '#2300F9' and genre == 'うれしい' :
                        st.header('おすすめ検索ワード:sunny')
                        
if color == '#2300F9' and genre == '怒っている' :
                            st.header('おすすめ検索ワード:tiger')
                            
if color == '#2300F9' and genre == '何も感じない' :
                          st.header('おすすめ検索ワード:deep sea') 
#の語彙
if color == '#f9e300' and genre == '楽しい' :
                  st.header('おすすめ検索ワード:happy')
                    
                    
if color == '#f9e300' and genre == '悲しい' :
                   st.header('おすすめ検索ワード:dry')
                       
if color == '#f9e300' and genre == 'うれしい' :
                      st.header('おすすめ検索ワード:sunny')
                        
if color == '#f9e300' and genre == '怒っている' :
                           st.header('おすすめ検索ワード:grill')
                            
if color == '#f9e300' and genre == '何も感じない' :
                            st.header('おすすめ検索ワード:starved')

st.title('Let’s tweet')
title = st.text_input('入力しよう', '（例）ものづくり')
st.header('TwitterURL↓')
st.write('https://twitter.com/home?lang=ja')                          
                                
                                
            
        


 
 
 