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
      <div className="back">
        <img src={sunflower.src} alt="result flower" />
      </div>

      {/* :TOもんちゃん  ここにcssを書いてね */}
      <style jsx>{`
        .back {
          background-color: rgb(255, 255, 255, 0.5);
          width: 100%;
          height: 100%;
        }
      `}</style>
    </>
  );
};
