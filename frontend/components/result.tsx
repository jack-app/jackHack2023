import React from "react";
import sunflower from "../public/sunflower.png";

interface ResultProps {
  result: {
    name: string;
    image: string;
    flower_symbolism: string;
    example: string;
  };
}

export const Result: React.FC<ResultProps> = (result) => {
  return (
    <>
      {/* :TOもんちゃん  ここにHTMLを書いてね */}
      <style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@300&display=swap');
</style>
      
      <div className="back">

        <img src={sunflower.src} alt="result flower" />

        <div className="contents">
         <div className="name">
          ひまわり
         </div>
         <div className="meaning">
          <span>花言葉</span>   私はあなただけを見つめています
         </div>
         <div className="examples">
          <span>贈る時のことば</span>     これからもずっとあなたを好きでいますよ。
         </div>
        </div>

      </div>




      {/* :TOもんちゃん  ここにcssを書いてね */}
      <style jsx>{`
      
       .contents {
         
       }
        .back {
          background-color: rgb(255, 255, 255, 0.5);
          width: 100%;
          height: 100%;
          display: flex;
          text-align: center;
        }
        .name {
          font-size: 70px;
          font-family: "Noto Serif JP", serif;
          padding-left: 50px;
          padding-top: 50px;
          font-weight: bold;
        }
        .meaning {
          font-size: 30px;
          font-family: "Noto Serif JP", serif;
          padding-left: 70px;
          padding-top: 80px;        
        }
        .meaning span {
          font-size: 45px;
          color: #F08080;
          font-family: "Noto Serif JP", serif;
          padding-right: 30px;
          display: block;
        }
        .examples {
          font-size: 30px;
          font-family: "Noto Serif JP", serif;
          padding-left: 80px;
          padding-top: 50px;
        }
        .examples span {
          font-size: 40px;
          color: #FF9966;
          padding-right: 30px;
          display: block;
        }
      `}</style>
    </>
  );
}
