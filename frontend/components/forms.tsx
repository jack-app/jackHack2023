import React from "react";

interface FormsProps {
  handleClick: () => void;
}

export const Forms: React.FC<FormsProps> = (props) => {
  const { handleClick } = props;

  return (
    <>
      <div className="forms">
        <div className="who">
          <div>誰に花を送りますか？</div>
          <input type="text" className="form-who" />
        </div>
        <div className="feel">
          <div>どんな気持ちを伝えますか？</div>
          <textarea className="form-feel" />
        </div>
        <button onClick={handleClick}>検索</button>
      </div>
      <style jsx>{`
        .forms {
          background-color: rgb(255, 255, 255, 0.3);
          width: 60%;
          height: 70%;
          padding: 2rem 7rem;
          display: flex;
          flex-direction: column;
          justify-content: space-around;
          align-items: flex-start;
        }

        .who {
          font-size: 1.5rem;
          font-family: serif;
          font-weight: 100;
        }

        .feel {
          font-size: 1.5rem;
          font-family: serif;
          font-weight: 100;
        }
      `}</style>
    </>
  );
};
