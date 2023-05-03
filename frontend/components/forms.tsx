import React from "react";

interface FormsProps {
  handleClick: () => void;
}

export const Forms: React.FC<FormsProps> = (props) => {
  const { handleClick } = props;

  return (
    <>
      <div className="forms">
        <button onClick={handleClick}>検索</button>
      </div>
      <style jsx>{`
        .forms {
          background-color: rgb(255, 255, 255, 0.3);
          width: 80%;
          height: 80%;
        }
      `}</style>
    </>
  );
};
