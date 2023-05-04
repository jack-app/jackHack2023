import React from "react";

export const Loading: React.FC = () => {
  return (
    <>
      <div className="loading">
        <div className="circle"></div>
        <div className="text">お花を摘んでいます...</div>
      </div>

      <style jsx>{`
        .text {
          position: absolute;
          padding-top: 160px;
          top: calc(50%);
          left: calc(50%);
          transform: translate(-50%, -50%);
          font-size: 1.5rem;
          font-family: serif;
          font-weight: 100;
        }
        .loading {
          opacity: 0.6;
          position: absolute;
          width: 100%;
          height: 100%;
          top: 0px;
          left: 0px;
        }

        .circle {
          width: 60px;
          height: 60px;
          border-radius: 150px;
          border: 5px solid #fff;
          border-top-color: rgba(0, 0, 0, 0.2);
          box-sizing: border-box;
          position: absolute;
          top: calc(50% - 30px);
          left: calc(50% - 30px);
          animation: circle 1s linear infinite;
        }
        @keyframes circle {
          0% {
            transform: rotate(0deg);
          }
          100% {
            transform: rotate(360deg);
          }
        }
        @-webkit-keyframes circle {
          0% {
            -webkit-transform: rotate(0deg);
          }
          100% {
            -webkit-transform: rotate(360deg);
          }
        }
      `}</style>
    </>
  );
};
