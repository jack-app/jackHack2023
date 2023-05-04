import React from "react";
import sunflower from "../public/sunflower.png";

interface ResultProps {
  name: string;
  image: string;
  flower_symbolism: string;
  example: string;
}

export const Result: React.FC<ResultProps> = (props) => {
  const { name, image, flower_symbolism, example } = props;

  return (
    <>
      <div className="back">
        <img src={image} alt="result flower" className="image" />

        <div className="contents">
          <div className="name">{name}</div>
          <div className="meaning">
            <span>花言葉</span> {flower_symbolism}
          </div>
          <div className="examples">
            <span>贈る時のことば</span> {example}
          </div>
        </div>
      </div>

      <style jsx>{`
        .back {
          background-color: rgb(255, 255, 255, 0.5);
          width: 100%;
          height: 100%;
          display: flex;
          flex-direction: row;
          justify-content: space-around;
          align-items: center;
          padding: 5% 10%;
        }

        .contents {
          padding-left: 64px;
        }

        .image {
          max-width: 40%;
          max-height: 80%;
        }
        .name {
          font-size: 64px;
          font-family: serif;
        }
        .meaning {
          font-size: 24px;
          font-family: serif;
          margin-top: 60px;
          font-weight: 100;
        }
        .meaning span {
          font-size: 36px;
          color: #f08080;
          font-family: serif;
          padding-right: 30px;
          display: block;
        }
        .examples {
          font-size: 24px;
          font-family: serif;
          padding-top: 50px;
          font-weight: 100;
        }
        .examples span {
          font-size: 36px;
          color: #ff9966;
          padding-right: 30px;
          display: block;
        }
      `}</style>
    </>
  );
};
