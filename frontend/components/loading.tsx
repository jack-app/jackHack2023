import React from "react";

export const Loading: React.FC = () => {
  return (
    <>
      <div className="loading">
        <div className="circle"></div>
      </div>

      <style jsx>{`
        .loading {
          opacity: 0.6;
          position: absolute;
          width: 400px;
          height: 200px;
          top: 0px;
          left: 0px;
        }

        .circle {
          width: 100px;
          height: 100px;
          border-radius: 150px;
          border: 15px solid #fff;
          border-top-color: rgba(0, 0, 0, 0.3);
          box-sizing: border-box;
          position: absolute;
          top: 20%;
          left: 35%;
          animation: circle 1s linear infinite;
          -webkit-animation: circle 1s linear infinite;
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
