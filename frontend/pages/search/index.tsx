import React, { useState } from "react";
import background from "../../public/background_image.png";
import { Result } from "../../components/result";
import { Forms } from "../../components/forms";
import { Loading } from "../../components/loading";
import axios from "axios";

interface ResultType {
  name: string;
  image: string;
  flower_symbolism: string;
  example: string;
}

export default function Search() {
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [result, setResult] = useState<ResultType | null>({
    name: "",
    image: "",
    flower_symbolism: "",
    example: "",
  });

  const handleClick = async () => {
    setIsLoading(true);
    await axios
      .post("http://127.0.0.1:5000", { content: { opponent: "お母さん", feeling: "感謝" } })
      .then((res) => {
        setResult(res.data);
        setIsLoading(false);
      })
      .catch((err) => {
        setIsLoading(false);
        alert(err);
        console.error(err);
      });
  };

  return (
    <>
      {
        <div className="container">
          {!isLoading && !result && <Forms handleClick={handleClick} />}
          {isLoading && <Loading />}
          {result && <Result result={result} />}
        </div>
      }

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
