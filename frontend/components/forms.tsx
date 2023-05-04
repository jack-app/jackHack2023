import React, { useRef } from "react";

interface FormsProps {
  handleClick: (opponent: string, feeling: string) => void;
}

export const Forms: React.FC<FormsProps> = (props) => {
  const { handleClick } = props;

  const whoRef = useRef<HTMLInputElement>(null);
  const feelRef = useRef<HTMLTextAreaElement>(null);

  const send = function () {
    const opponent = whoRef.current?.value;
    const feeling = feelRef.current?.value;
    if (opponent && feeling) {
      handleClick(opponent, feeling);
    }

    if (!opponent) alert("誰に花を送りますか？");
    if (!feeling) alert("どんな気持ちを伝えますか？");
  };

  return (
    <>
      <div className="forms">
        <div className="who">
          <div>誰に花を送りますか？</div>
          <input type="text" className="form-who" ref={whoRef} />
        </div>
        <div className="feel">
          <div>どんな気持ちを伝えますか？</div>
          <textarea className="form-feel" ref={feelRef} />
        </div>
        <button onClick={send} className="search">
          検索
        </button>
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
          width: 100%;
          font-size: 1.5rem;
          font-family: serif;
          font-weight: 100;
        }

        .form-who {
          width: 100%;
          border: none;
          border-bottom: solid 1px #898989;
          background-color: rgba(255, 255, 255, 0.55);
          font-size: 1.2rem;
          font-family: serif;
          font-weight: 100;
          padding: 10px;
          margin-top: 20px;
          transition: all 0.3s ease;
        }

        .form-who:focus {
          outline: none;
          border-bottom: solid 1px #629eff;
          background-color: rgba(255, 255, 255, 0.9);
        }

        .feel {
          font-size: 1.5rem;
          font-family: serif;
          font-weight: 100;
          width: 100%;
        }

        .form-feel {
          resize: none;
          width: 100%;
          border: none;
          border-bottom: solid 1px #898989;
          background-color: rgba(255, 255, 255, 0.55);
          font-family: serif;
          font-weight: 100;
          font-size: 1.2rem;
          padding: 10px;
          margin-top: 20px;
          transition: all 0.3s ease;
        }

        .form-feel:focus {
          transform: translate();
          outline: none;
          border-bottom: solid 1px #629eff;
          background-color: rgba(255, 255, 255, 0.9);
        }

        .search {
          margin-left: auto;
          margin-right: auto;
          font-family: serif;
          font-weight: 100;
          font-size: 1.2rem;
          letter-spacing: 2px;
          border: none;
          box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
          background-color: rgba(255, 255, 255, 0.95);
          border-radius: 5px;
          padding: 8px 16px;
          transition: all 0.3s ease;
        }

        .search:hover {
          cursor: pointer;
          background-color: rgba(255, 255, 255, 1);
          box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.5);
        }
      `}</style>
    </>
  );
};
