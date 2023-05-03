import Head from "next/head";
import background from "../public/background_image.png";

export default function Home() {
  return (
    <>
      <div className="container">
        <div className="titles">
          <h1 className="title">タイトル</h1>
          <h2 className="subtitle">サブタイトル</h2>
        </div>
        <div className="start">
          <button className="button">Start</button>
        </div>
      </div>

      <style jsx>{`
        .container {
          width: 100%;
          height: 100vh;
          background-image: url(${background.src});
          background-size: cover;
          overflow: hidden;
        }

        .titles {
          width: 50%;
          background-color: rgb(255, 255, 255, 0.3);
          margin-top: 8%;
          margin-left: auto;
          margin-right: auto;
          display: flex;
          flex-direction: column;
          align-items: center;
          padding: 2rem;
        }
        .title {
          font-size: 4rem;
          font-family: serif;
          font-weight: 100;
        }

        .subtitle {
          font-size: 1.5rem;
          font-family: serif;
          font-weight: 100;
        }

        .start {
          margin-top: 8%;
          text-align: center;
        }
        .button {
          border: none;
          background: linear-gradient(
            left,
            rgb(255, 255, 255, 0.1),
            rgb(255, 255, 255, 0.7),
            rgb(255, 255, 255, 0.1)
          );
          font-size: 2rem;
          letter-spacing: 3px;
          font-family: serif;
          font-weight: 100;
          padding: 1rem 2rem;
          width: 40%;
        }

        .button:hover {
          cursor: pointer;
          background: linear-gradient(
            left,
            rgb(255, 255, 255, 0.2),
            rgb(255, 255, 255, 0.8),
            rgb(255, 255, 255, 0.2)
          );
        }
      `}</style>
    </>
  );
}
