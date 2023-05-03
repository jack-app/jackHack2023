import React from "react";
import background from "../../public/background_image.png";
import { Result } from "../../components/result";
import { Forms } from "../../components/forms";
import { Loading } from "../../components/loading";

export default function Search() {
  return (
    <>
      <div className="container">
        <Forms />
        <Loading />
        <Result />
      </div>

      <style jsx>{`
        .container {
          width: 100%;
          height: 100vh;
          background-image: url(${background.src});
          background-size: cover;
          overflow: hidden;
          display: flex;
          justify-content: center;
          align-items: center;
        }
      `}</style>
    </>
  );
}
